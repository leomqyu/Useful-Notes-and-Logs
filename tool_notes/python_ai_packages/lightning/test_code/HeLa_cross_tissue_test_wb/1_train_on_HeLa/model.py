import fm  # for development with RNA-FM
# from pathlib import Path

import torch
import torch.nn as nn
import torch.nn.functional as F

import numpy as np

import lightning as pl

# from torchmetrics import AUROC, AveragePrecision
from torchmetrics.classification import BinaryAUROC, BinaryAveragePrecision

class siteLevelModel(pl.LightningModule):  # change
    def __init__(self, seq_len=128, mode='fm_seq', 
                 lr=1e-3, weight_decay=1e-4, 
                 num_uc_conv_layers=1, kernel_size_se=11, kernel_size_oh=5, dropout_prob=0.1,
                 pos_weight_ratio=87.5):

        super().__init__()
        
        # self.pos_weight = torch.tensor([pos_weight_ratio]).to(None)
        # print('self.pos_weight is on ', self.pos_weight.device)

        self.seq_len = seq_len
        self.lr = lr
        self.weight_decay = weight_decay
        # print(self.device)
        # input('...')
        self.register_buffer('pos_weight', torch.full((self.seq_len, 1), pos_weight_ratio))
        # self.pos_weight = torch.tensor([pos_weight_ratio for _ in range(seq_len)]).to(self.device)

        # define the metric for each position in the sequence
        self.train_auroc_metric = BinaryAUROC()
        self.train_auprc_metric = BinaryAveragePrecision()

        self.val_auroc_metric = BinaryAUROC()
        self.val_auprc_metric = BinaryAveragePrecision()

        self.train_loss = []
        self.val_loss = []

        if mode == 'fm_seq':  # use FM embedding + sequence ont-hot encoding in a single branch, (B, L, 640 + 4)

            '''fm'''
            self.fm_model, self.alphabet = fm.pretrained.rna_fm_t12()
            self.batch_converter = self.alphabet.get_batch_converter()
            # self.fm_model.cuda()  # use GPU if available
            self.fm_model.eval()
            # print('fm.device(): ', next(self.fm_model.parameters()).device)       # gpu

            for param in self.fm_model.parameters():
                param.requires_grad = False

            '''seq emb CNN'''
            self.conv_se_1 = nn.Conv1d(in_channels=640, out_channels=1024, kernel_size=kernel_size_se,
                                       padding=(kernel_size_se - 1) // 2)
            self.dropout_se_1 = nn.Dropout(
                p=dropout_prob)  # By randomly dropping neurons,
            # dropout forces the network to learn more robust features that are not reliant on the presence of specific neurons.
            # This helps in generalizing better to unseen data.

            self.non_change_conv_layers = nn.ModuleList([
                nn.Conv1d(in_channels=1024, out_channels=1024, kernel_size=kernel_size_se,
                          padding=(kernel_size_se - 1) // 2) for i in range(num_uc_conv_layers)
            ])
            self.non_change_dropouts = nn.ModuleList([nn.Dropout(p=dropout_prob) for _ in range(num_uc_conv_layers)])

            self.conv_se_2 = nn.Conv1d(in_channels=1024, out_channels=512, kernel_size=kernel_size_se,
                                       padding=(kernel_size_se - 1) // 2)
            self.dropout_se_2 = nn.Dropout(p=dropout_prob)

            # self.conv_se_3 = nn.Conv1d(in_channels=512, out_channels=256, kernel_size=kernel_size, padding=(kernel_size-1)//2)
            self.conv_se_4 = nn.Conv1d(in_channels=512, out_channels=128, kernel_size=kernel_size_se,
                                       padding=(kernel_size_se - 1) // 2)
            self.dropout_se_4 = nn.Dropout(p=dropout_prob)

            # self.conv_se_5 = nn.Conv1d(in_channels=128, out_channels=64, kernel_size=kernel_size, padding=(kernel_size-1)//2)
            self.conv_se_6 = nn.Conv1d(in_channels=128, out_channels=32, kernel_size=kernel_size_se,
                                       padding=(kernel_size_se - 1) // 2)
            self.dropout_se_6 = nn.Dropout(p=dropout_prob)

            # self.conv_se_7 = nn.Conv1d(in_channels=32, out_channels=16, kernel_size=kernel_size, padding=(kernel_size-1)//2)
            self.conv_se_8 = nn.Conv1d(in_channels=32, out_channels=1, kernel_size=kernel_size_se,
                                       padding=(kernel_size_se - 1) // 2)
            self.dropout_se_8 = nn.Dropout(p=dropout_prob)

            '''seq emb fc'''
            self.fc_se_1 = nn.Linear(seq_len, seq_len)
            self.fc_se_dropout1 = nn.Dropout(p=dropout_prob)
            self.fc_se_2 = nn.Linear(seq_len, seq_len)
            self.fc_se_dropout2 = nn.Dropout(p=dropout_prob)

            '''one-hot CNN'''
            # self.conv_oh_1 = nn.Conv1d(in_channels=4, out_channels=4, kernel_size=kernel_size_oh, padding=(kernel_size_oh-1)//2)
            # self.dropout_oh_1 = nn.Dropout(p=dropout_prob)
            self.conv_oh_2 = nn.Conv1d(in_channels=4, out_channels=1, kernel_size=kernel_size_oh,
                                       padding=(kernel_size_oh - 1) // 2)
            self.dropout_oh_2 = nn.Dropout(p=dropout_prob)

            '''merge CNN'''
            self.merge = nn.Conv1d(in_channels=2, out_channels=1, kernel_size=1, padding=0)
            self.dropout_merge = nn.Dropout(p=dropout_prob)

            print(
                f'Model init finished. num_uc_conv_layers = {num_uc_conv_layers}, kernel_size_se = {kernel_size_se}, '
                f'kernel_size_oh = {kernel_size_oh} dropout_prob={dropout_prob}')

        else:
            raise ValueError(f'[error] unsupported input data mode: {mode}')

        self.mode = mode

        # self._initialize_weights()    

    def forward(self, x):

        # if self.mode == 'fm_seq':
        '''fm'''
        x = self.encode_seq(x)

        '''split x to seq-emb and one-hot'''
        x_oh = x[:, :, 640:644].permute(0, 2, 1)  # [B, 4, 128]
        x_seq_emb = x[:, :, 0:640].permute(0, 2, 1)  # [B, 640, 128]

        '''seq emb CNN'''
        x_seq_emb = F.relu(self.conv_se_1(x_seq_emb))
        x_seq_emb = self.dropout_se_1(x_seq_emb)

        for conv_layer, dropout in zip(self.non_change_conv_layers, self.non_change_dropouts):
            x_seq_emb = F.relu(conv_layer(x_seq_emb))
            x_seq_emb = dropout(x_seq_emb)

        x_seq_emb = F.relu(self.conv_se_2(x_seq_emb))
        x_seq_emb = self.dropout_se_2(x_seq_emb)
        x_seq_emb = F.relu(self.conv_se_4(x_seq_emb))
        x_seq_emb = self.dropout_se_4(x_seq_emb)
        x_seq_emb = F.relu(self.conv_se_6(x_seq_emb))
        x_seq_emb = self.dropout_se_6(x_seq_emb)
        x_seq_emb = F.relu(self.conv_se_8(x_seq_emb))
        x_seq_emb = self.dropout_se_8(x_seq_emb).squeeze(dim=1)  # [B, 128]

        '''seq emb fc'''
        x_seq_emb = F.relu(self.fc_se_1(x_seq_emb))
        x_seq_emb = self.fc_se_dropout1(x_seq_emb)
        x_seq_emb = F.relu(self.fc_se_2(x_seq_emb)).unsqueeze(dim=1)
        x_seq_emb = self.fc_se_dropout2(x_seq_emb)  # [B, 1, 128]

        '''one-hot CNN'''
        x_oh = F.relu(self.conv_oh_2(x_oh))
        x_oh = self.dropout_oh_2(x_oh)  # [B, 1, 128]

        '''merge'''
        x_merged = torch.cat((x_seq_emb, x_oh), dim=1)
        x_merged = self.merge(x_merged).squeeze(dim=1)  # [B, 128]
        x_merged = self.dropout_merge(x_merged)  # [B, 128]

        return x_merged

    def encode_seq(self, seqs):
        """gen_rna_fm_encoding"""
        embs = []

        for seq in seqs:
            '''gen fm emb'''
            _, _, tokens = self.batch_converter([('input', seq)])
            with torch.no_grad():
                output = self.fm_model(tokens.to(self.device), repr_layers=[12])
            fm_emb = output['representations'][12][:, 1:-1, :]  # (1, L, 640)

            '''gen seq emb'''
            seq_emb = self.one_hot_encode_rna(seq)  # (L, 4)
            seq_emb = np.expand_dims(seq_emb, axis=0)  # (1, L, 4)

            '''concat final emb'''
            emb = torch.cat([fm_emb, torch.tensor(seq_emb).to(self.device).float()], dim=2)
            embs.append(emb)

        embs = torch.cat(embs, dim=0)
        return embs

    @staticmethod
    def one_hot_encode_rna(rna_sequence):
        mapping = {'A': 0, 'C': 1, 'G': 2, 'U': 3}

        # Initialize one-hot encoded array
        one_hot_encoded = np.zeros((len(rna_sequence), len(mapping)))

        # Convert sequence to integer representation
        for i, nucleotide in enumerate(rna_sequence):
            if nucleotide in mapping:
                one_hot_encoded[i, mapping[nucleotide]] = 1

        return one_hot_encoded

    def training_step(self, batch, batch_idx):
        names, inputs, target = batch
        output = self(inputs)

        # swap the dimensions of the output tensor
        output = torch.transpose(output, 0, 1)
        target = torch.transpose(target, 0, 1)

        # print(output.shape, target.shape, self.pos_weight.shape)
        # input('train...')

        # pos_weight = torch.full((self.seq_len,), self.pos_weight_ratio).to('cuda')
        loss = torch.nn.functional.binary_cross_entropy_with_logits(output, target.float(), pos_weight=self.pos_weight)

        # calculate the AUROC and AUPRC
        # the sigmoid operation will be performed within the metrics

        output = torch.transpose(output, 0, 1)
        target = torch.transpose(target, 0, 1)

        self.train_auroc_metric.update(output, target.int())
        self.train_auprc_metric.update(output, target.int())

        self.train_loss.append(loss.item())

        return loss

    def on_train_epoch_end(self):
        auroc_scores = self.train_auroc_metric.compute()
        auprc_scores = self.train_auprc_metric.compute()

        # store the latest metric scores
        # self.latest_auroc_scores[self.current_epoch] = auroc_scores
        # self.latest_auprc_scores[self.current_epoch] = auprc_scores

        # log average scores
        self.log('train_auroc', torch.mean(auroc_scores), sync_dist=True, prog_bar=True)
        self.log('train_auprc', torch.mean(auprc_scores), sync_dist=True, prog_bar=True)

        # reset metrics
        self.train_auroc_metric.reset()
        self.train_auprc_metric.reset()

        # log average loss
        self.log('train_loss', np.mean(self.train_loss), sync_dist=True, prog_bar=True)

        self.train_loss = []

    def validation_step(self, batch, batch_idx):
        names, inputs, target = batch
        output = self(inputs)

        # calculate the AUROC and AUPRC
        # the sigmoid operation will be performed within the metrics

        # swap the dimensions of the output tensor
        output = torch.transpose(output, 0, 1)
        target = torch.transpose(target, 0, 1)

        self.val_auroc_metric.update(output, target.int())
        self.val_auprc_metric.update(output, target.int())

        loss = torch.nn.functional.binary_cross_entropy_with_logits(output, target.float(), pos_weight=self.pos_weight)

        self.val_loss.append(loss.item())

    def on_validation_epoch_end(self):
        auroc_scores = self.val_auroc_metric.compute()
        auprc_scores = self.val_auprc_metric.compute()

        # store the latest metric scores
        # self.latest_auroc_scores[self.current_epoch] = auroc_scores
        # self.latest_auprc_scores[self.current_epoch] = auprc_scores

        # log average scores
        self.log('val_auroc', torch.mean(auroc_scores), sync_dist=True, prog_bar=True)
        self.log('val_auprc', torch.mean(auprc_scores), sync_dist=True, prog_bar=True)

        # reset metrics
        self.val_auroc_metric.reset()
        self.val_auprc_metric.reset()

        # log average loss
        self.log('val_loss', np.mean(self.val_loss), sync_dist=True, prog_bar=True)

        self.val_loss = []

    def test_step(self, batch, batch_idx):
        names, inputs, target = batch
        output = self(inputs)

        # swap the dimensions of the output tensor
        output = torch.transpose(output, 0, 1)
        target = torch.transpose(target, 0, 1)

        self.val_auroc_metric.update(output, target.int())
        self.val_auprc_metric.update(output, target.int())

    def on_test_epoch_end(self):
        auroc_scores = self.val_auroc_metric.compute()
        auprc_scores = self.val_auprc_metric.compute()

        # log average scores
        self.log('test_auroc', torch.mean(auroc_scores), sync_dist=True, prog_bar=True)
        self.log('test_auprc', torch.mean(auprc_scores), sync_dist=True, prog_bar=True)

        # reset metrics
        self.val_auroc_metric.reset()
        self.val_auprc_metric.reset()
        

    def configure_optimizers(self):
        optimizer = torch.optim.Adam(self.parameters(), lr=self.lr, weight_decay=self.weight_decay)
        # scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=30, gamma=0.1)

        return optimizer

from pathlib import Path
import torch
import numpy as np
import random
from dataset import RNAModDataModule
from model import siteLevelModel
import argparse
import lightning as pl
from lightning.pytorch import seed_everything
from lightning.pytorch.callbacks import ModelCheckpoint
from pytorch_lightning.loggers import WandbLogger
from utils import read_fasta, count_pos_weight
import os
from datetime import datetime


def main():
    """read argument"""
    '''read'''
    parser = argparse.ArgumentParser(description='simple distributed training job')

    parser.add_argument('--work_base', type=str, help='CUDA visible devices (default: 0)')
    parser.add_argument('--data_dir', type=str, help='CUDA visible devices (default: 0)')

    parser.add_argument('--gpu', nargs='+', type=int, default=[0], help='CUDA visible devices (default: 0)')
    parser.add_argument('--seq_len', default=128, type=int, help='Total epochs to train the model')
    # parser.add_argument('--fold', type=int, help='How often to save a snapshot')

    parser.add_argument('--batch_size', default=256, type=int, help='Input batch size on each device (default: 32)')
    parser.add_argument('--lr', default=1e-3, type=float, help='Input batch size on each device (default: 32)')
    parser.add_argument('--weight_decay', default=1e-2, type=float,
                        help='Input batch size on each device (default: 32)')

    parser.add_argument('--epochs', default=1000, type=int, help='Total epochs to train the model')
    parser.add_argument('--save_every', type=int, help='How often to save a snapshot')

    args = parser.parse_args()

    '''parse'''
    ''''dir related'''
    work_base = args.work_base
    print(f'work_base: {work_base}')

    data_dir = args.data_dir
    print(f'Getting data from: {data_dir}')

    results_dir = Path(work_base, '1_train_on_HeLa/results')
    model_dir = Path(results_dir, 'models')
    os.makedirs(model_dir, exist_ok=True)

    ''''cuda'''
    cuda_visible_devices = ','.join(map(str, args.gpu))
    print(f'cuda_visible_devices: ', cuda_visible_devices)
    os.environ['CUDA_VISIBLE_DEVICES'] = cuda_visible_devices

    ''''training hyper param'''
    batch_size = args.batch_size
    lr = args.lr
    weight_decay = args.weight_decay
    epochs = args.epochs

    ''''others'''
    seq_len = args.seq_len
    save_every = args.save_every

    """init"""
    seed_everything(42, workers=True)
    torch.set_float32_matmul_precision('high')

    """find pos weight"""
    train_path = Path(data_dir, f'fold0_train.fasta')
    _, y_train = read_fasta(train_path, seq_len)
    pos_weight_ratio = count_pos_weight(y_train)
    print(f'pos weight ratio: {pos_weight_ratio}', flush=True)

    """train"""
    project_name = datetime.now().strftime("%m-%d-%H-%M")  # string format time
    wandb_logger = WandbLogger(project=f'{project_name}_train')
    
    data_module = RNAModDataModule(data_dir, batch_size)

    model = siteLevelModel(seq_len, lr=lr, weight_decay=weight_decay, pos_weight_ratio=pos_weight_ratio)

    '''checkpoint save config'''
    checkpoint_callback = ModelCheckpoint(dirpath=model_dir, filename='{epoch:02d}-{val_loss:.2f}', every_n_epochs=save_every, save_top_k=-1)        # save every epoch
    # checkpoint_callback = ModelCheckpoint(dirpath=model_dir, monitor='val_loss', filename='{epoch:02d}-{val_loss:.2f}', every_n_epochs=1, save_top_k=1)        # save best epoch

    trainer = pl.Trainer(deterministic=False,
                         logger=wandb_logger,
                         max_epochs=epochs, 
                         default_root_dir = results_dir,        # save the lightning_log
                         callbacks=[checkpoint_callback],       # save the checkpoint
                         accelerator='auto', devices='auto', strategy='auto')
    
    trainer.fit(model=model, train_dataloaders=data_module)

    '''finishing'''
    wandb.finish()


if __name__ == '__main__':
    main()

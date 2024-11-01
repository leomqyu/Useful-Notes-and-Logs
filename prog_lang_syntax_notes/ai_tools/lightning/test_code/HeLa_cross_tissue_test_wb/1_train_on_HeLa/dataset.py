from pathlib import Path

import torch
# from lightning.pytorch.utilities.types import TRAIN_DATALOADERS
from torch.utils.data import Dataset, DataLoader

import lightning as pl

from utils import read_fasta


class RNAModDataset(Dataset):
    def __init__(self, fasta_path):
        super().__init__()

        seq_list, self.labels = read_fasta(fasta_path)

        self.seq_names = [seq_info[0] for seq_info in seq_list]  # list of str
        self.seqs = [seq_info[1] for seq_info in seq_list]  # list of str

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):

        name = self.seq_names[idx]
        seq = self.seqs[idx]
        label = torch.tensor(self.labels[idx], dtype=torch.float)

        return name, seq, label


class RNAModDataModule(pl.LightningDataModule):
    def __init__(self, data_dir, batch_size=64, num_workers=24):
        super().__init__()

        self.num_workers = num_workers

        self.data_dir = data_dir
        self.batch_size = batch_size

        # pre-initialize the datasets
        self.train_dataset = None
        self.val_dataset = None
        self.test_dataset = None


    def setup(self, stage):
        """
        stage (str): 'fit' or 'test'
        """
        train_fasta_path = Path(self.data_dir, 'fold0_train.fasta')
        val_fasta_path = Path(self.data_dir, 'fold0_test.fasta')
        # test_fasta_path = Path(self.data_dir, 'test.fasta')
        test_fasta_path = Path(self.data_dir, 'all_seq.fasta')

        self.train_dataset = RNAModDataset(train_fasta_path)
        self.val_dataset = RNAModDataset(val_fasta_path)
        # self.test_dataset = RNAModDataset(test_fasta_path)
        self.test_dataset = RNAModDataset(test_fasta_path)

    def train_dataloader(self):
        return DataLoader(self.train_dataset, batch_size=self.batch_size, shuffle=True, num_workers=self.num_workers)

    def val_dataloader(self):
        return DataLoader(self.val_dataset, batch_size=self.batch_size, shuffle=False, num_workers=self.num_workers)

    def test_dataloader(self):
        return DataLoader(self.test_dataset, batch_size=self.batch_size, shuffle=False, num_workers=self.num_workers)

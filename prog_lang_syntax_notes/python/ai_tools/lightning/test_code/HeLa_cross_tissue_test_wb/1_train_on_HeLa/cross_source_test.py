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
    parser = argparse.ArgumentParser()

    parser.add_argument('--work_base', type=str)
    parser.add_argument('--source', type=str)
    parser.add_argument('--test_dir', type=str)
    parser.add_argument('--model_path', type=str)
    parser.add_argument('--gpu', nargs='+', type=int, default=[0])
    parser.add_argument('--seq_len', default=128, type=int)
    parser.add_argument('--batch_size', default=256, type=int)

    args = parser.parse_args()

    '''parse'''
    ''''dir related'''
    work_base = args.work_base
    print(f'work_base: {work_base}')

    data_dir = args.test_dir
    print(f'Getting testing data from: {data_dir}')

    model_path = Path(work_base, args.model_path)
    print(f'Test model is from: {model_path}')

    source = args.source
    results_dir = Path(work_base, '1_train_on_HeLa/results')
    test_source_dir = Path(results_dir, f'test_{source}')
    os.makedirs(test_source_dir, exist_ok=True)

    ''''cuda'''
    cuda_visible_devices = ','.join(map(str, args.gpu))
    print(f'cuda_visible_devices: ', cuda_visible_devices)
    os.environ['CUDA_VISIBLE_DEVICES'] = cuda_visible_devices

    ''''training hyper param'''
    batch_size = args.batch_size
    seq_len = args.seq_len

    """init"""
    seed_everything(42, workers=True)
    torch.set_float32_matmul_precision('high')

    """train"""
    current_time = datetime.now().strftime("%m-%d-%H-%M")  # string format time
    wandb_logger = WandbLogger(project=f'test_{source}_{current_time}')

    data_module = RNAModDataModule(data_dir, batch_size)

    pretrained_model = siteLevelModel.load_from_checkpoint(checkpoint_path=model_path, map_location=None, seq_len=seq_len)

    trainer = pl.Trainer(deterministic=False,
                         devices=1,
                         logger=wandb_logger,
                         default_root_dir = results_dir,
                         accelerator='auto', strategy='auto')

    trainer.test(model=pretrained_model, datamodule=data_module)

    '''finishing'''
    wandb.finish()


if __name__ == '__main__':
    main()

from Bio import SeqIO  # for file parsing
import numpy as np
import torch

from torchmetrics import Metric
from torchmetrics.functional import accuracy, precision, recall


def count_pos_weight(labels):
    labels_tensor = torch.tensor(labels)  # Convert the labels list to a PyTorch tensor

    if labels_tensor.dtype != torch.long:
        raise ValueError(f"The data type of labels_tensor: {labels_tensor.dtype} is not integer as expected.")

    total_positives = torch.sum(labels_tensor == 1)
    total_negatives = torch.numel(labels_tensor) - total_positives

    ratio = total_negatives.float() / total_positives

    return ratio


def read_fasta(fasta_path, seq_len=128):
    """input fasta path, output a list of [(seq_name, seq)] and a list of labels"""

    records = list(SeqIO.parse(fasta_path, 'fasta'))

    seqs = [str(record.seq) for record in records]
    names = [record.id for record in records]

    # get the labels for each sequence
    labels = []

    for name in names:
        # each label should be a vector of 0s and 1s specifying the modification sites
        seq_label_array = np.zeros((seq_len,), dtype=int)

        if name[0] == '1':  # this sequence contains positive modification sites
            sites_list = [int(site_idx) for site_idx in name.split('--')[8].split(',')]
            seq_label_array[sites_list] = 1

        labels.append(seq_label_array)

    seq_list = [(seq_name, seq) for seq_name, seq in zip(names, seqs)]

    return seq_list, labels





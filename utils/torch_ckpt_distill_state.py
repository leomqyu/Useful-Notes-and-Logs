"""
sample:
    python distill_ckpt.py --input "path/to/large_file.ckpt" --output "path/to/distilled.ckpt"
"""

import torch
import os

def distill_checkpoint(input_ckpt_path, output_ckpt_path):
    """
    Extracts only model weights from a .ckpt file and saves a lighter version.
    
    Args:
        input_ckpt_path (str): Path to the input .ckpt file.
        output_ckpt_path (str): Path to save the distilled .ckpt file.
    """
    # Load the full checkpoint
    checkpoint = torch.load(input_ckpt_path, map_location='cpu', weights_only=True)
    
    # Extract only the model state dict (discard optimizer/hyperparameters)
    distilled_state = {
        'state_dict': checkpoint['state_dict']  # Assumes standard PyTorch Lightning format
    }
    
    # Save the distilled version
    torch.save(distilled_state, output_ckpt_path)
    
    # Print compression stats
    original_size = os.path.getsize(input_ckpt_path) / (1024 ** 2)  # MB
    new_size = os.path.getsize(output_ckpt_path) / (1024 ** 2)      # MB
    print(f"Distilled checkpoint saved to: {output_ckpt_path}")
    print(f"Size reduced from {original_size:.2f} MB → {new_size:.2f} MB (-{100 * (1 - new_size/original_size):.1f}%)")

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, required=True, help='Input .ckpt file path')
    parser.add_argument('--output', type=str, required=True, help='Output distilled .ckpt path')
    args = parser.parse_args()
    
    distill_checkpoint(args.input, args.output)
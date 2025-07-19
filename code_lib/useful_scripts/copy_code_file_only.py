"""
Only copy the files for backup, ignore the large data files
"""

import os
import shutil
from pathlib import Path
from tqdm import tqdm

src_dir = '/share/home/Andrew/leo'    # parent dir for backup
dst_dir = '/share/home/Andrew/leo/backup/backup_all_code_only'

def copy_code_files(src_dir, dst_dir, code_extensions, data_extensions):
    """
    Recursively copy code files preserving directory structure
    while ignoring data files and empty directories.
    """
    src_path = Path(src_dir).resolve()      # resolves into absolute path
    dst_path = Path(dst_dir).resolve()
    
    for root, _, files in tqdm(os.walk(src_path)):
        # print(root, dirs, files)
        current_dir = Path(root)
        relative_path = current_dir.relative_to(src_path)
        
        for file in files:
            file_ext = Path(file).suffix.lower()
            
            if file_ext in code_extensions and file_ext not in data_extensions:
                src_file = current_dir / file
                dest_dir = dst_path / relative_path
                
                # Create destination directory if it doesn't exist
                dest_dir.mkdir(parents=True, exist_ok=True)
                
                # Copy the file
                shutil.copy2(src_file, dest_dir)
                # print(f"Copied: {src_file} -> {dest_dir/ file}")

if __name__ == "__main__":
    code_extensions = {'.py', '.sh', '.ipynb', '.r', '.js', '.html', 
                      '.css', '.java', '.cpp', '.c', '.h', '.php', 
                      '.sql', '.json', '.xml', '.md', '.txt'}
    
    data_extensions = {'.npy', '.h5', '.hdf5', '.csv', '.tsv', 
                      '.xlsx', '.xls', '.mat', '.pkl', '.jpg', 
                      '.jpeg', '.png', '.gif', '.mp3', '.wav', 
                      '.mp4', '.avi', '.zip', '.tar', '.gz', '.ckpt'}        # just for check

    if not Path(src_dir).exists():
        print(f"Error: Source directory '{src_dir}' does not exist.")
        exit(1)

    copy_code_files(src_dir, dst_dir, code_extensions, data_extensions)
    print("\nFile copy completed! Directory structure preserved.")
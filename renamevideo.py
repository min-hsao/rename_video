# rename_videos.py
# by Min-Hsao Chen (w/ chatGPT-4o)
# v0.0002
# Last updated: 2024-06-11

import os
import sys
import argparse
from datetime import datetime
import shutil

def get_creation_time(file_path):
    return os.path.getctime(file_path)

def rename_files(directory, filter_text, new_name, outdir, dry_run):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and not f.startswith('.') and (filter_text in f if filter_text else True)]
    files.sort(key=lambda x: get_creation_time(os.path.join(directory, x)))
    
    print(f"Script: rename_videos.py, Version: v0.0002")
    
    if not outdir:
        outdir = directory

    if not os.path.exists(outdir):
        os.makedirs(outdir)

    if not files:
        print("No files to rename.")
        return

    for idx, filename in enumerate(files):
        file_extension = os.path.splitext(filename)[1]
        new_filename = f"{new_name}-{idx + 1}{file_extension}"
        old_file_path = os.path.join(directory, filename)
        new_file_path = os.path.join(outdir, new_filename)
        
        if dry_run:
            print(f"Would rename: {old_file_path} -> {new_file_path}")
        else:
            shutil.move(old_file_path, new_file_path)
            print(f"Renamed: {old_file_path} -> {new_file_path}")

    if not dry_run:
        print("File renaming completed.")

def main():
    parser = argparse.ArgumentParser(description="Rename video files based on their creation time.")
    parser.add_argument("directory", help="Directory containing the video files.")
    parser.add_argument("new_name", help="New filename pattern.")
    parser.add_argument("--filter", help="Text to filter which files to rename.", default="")
    parser.add_argument("--outdir", help="Output directory for renamed files.", default="")
    parser.add_argument("--dry_run", action="store_true", help="Show what would be renamed without actually renaming.")
    
    args = parser.parse_args()
    
    rename_files(args.directory, args.filter, args.new_name, args.outdir, args.dry_run)

if __name__ == "__main__":
    main()

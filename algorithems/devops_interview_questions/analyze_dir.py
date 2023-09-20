import os
import shutil


def analyze_directory(directory):
    total_files = 0
    total_size = 0
    # Walk through the directory and its subdirectories
    for root, _, files in os.walk(directory):
        for file in files:
          file_path = os.path.join(root,file)
          total_files += 1
          # Get size
          file_size = os.path.getsize(file_path)
          # Add sie to total
          total_size += file_size
    # Print the results
    print(f"total number of files: {total_files}")
    print(f"total size of all files: {total_size}")

# Prompt the user for the directory path
directory_path = input("Enter the directory path to analyze: ")

# Call the analyze_directory function with the provided input
analyze_directory(directory_path)

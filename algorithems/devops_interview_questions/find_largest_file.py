
import os

def find_largest_file(directory):
  largest_file = None
  largest_size = 0
  total = 0
  
  for root, _,files in os.walk(directory):
    for file in files:
      total += 1
      file_path = os.path.join(root, file)
      file_size = os.path.getsize(file_path)
      if file_size > largest_size:
        largest_file = file_path
        largest_size = file_size
  return largest_file, largest_size, total

if __name__ == "__main__":
    target_directory = input(f"input directory: ")
    largest_file, largest_size, total = find_largest_file(target_directory)
    if largest_file:
        # If a largest file is found, print its path and size
        print(f"\nscanned {total} files.")
        print(f"\nThe largest file is {largest_file} with a size of {largest_size} bytes.\n")
    else:
        # If no files are found in the specified directory, print a message
        print(f"scanned {total} files.")
        print("No files found in the specified directory.")
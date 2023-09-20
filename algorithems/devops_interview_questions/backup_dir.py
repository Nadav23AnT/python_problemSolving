import datetime
import os
import shutil


def create_backup(source, destination):
  timestamp = datetime.now().strftime("%Y-%m-%d_%H%M")
  backup_folder = os.path.join(destination, f"backup_{timestamp}")
  try:
    os.makedirs(backup_folder)
    for item in os.listdir(source):
      source_item = os.path.join(source, item)
      dest_item = os.path.join(backup_folder, item)
      
      if os.path.isdir(source_item):
        shutil.copytree(source_item, dest_item)
      else:
        shutil.copy2(source_item, dest_item)
    print(f"Backup created in: {backup_folder}")
  except Exception as e:
    print(f"An Error Occurred: {str(e)}")


source_directory = input() # "/path/to/source"
destination_directory = input() # "/path/to/backup"
create_backup(source_directory, destination_directory)
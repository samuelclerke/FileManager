from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path
import os
import shutil
import time
from time import strftime

class Handler(FileSystemEventHandler):
  def __init__(self, extensions):
    super().__init__()
    self.extensions = extensions

  def on_modified(self, event):
    self.downloadsDirProcessor(self.extensions)
  
  def on_created(self, event):
    pass

  def on_deleted(self, event):
    pass

  def downloadsDirProcessor(self, extensions: dict):
    downloadsPath = Path.home() / "Downloads"
    documentsPath = Path.home() / "Documents"
    recentlyDownloaded = documentsPath / "Recently Downloaded"

    # Create main directory if it doesn't exist
    recentlyDownloaded.mkdir(exist_ok=True)

    # Define folder mapping for extensions
    folder_map = {
        'executable': 'Executables',
        'compressed': 'Compressed & Zipped',
        'video': 'Videos',
        'image': 'Images & Pictures',
        'document': 'Documents',
        'audio': 'Music & Audio'
    }

    # Create subdirectories if they don't exist
    for folder in folder_map.values():
        (recentlyDownloaded / folder).mkdir(exist_ok=True)

    # Process downloaded files
    for file in downloadsPath.iterdir():
        if not file.is_file():
            continue  # Skip directories

        renameTime = strftime("%H_%M_%S")  # Time format to avoid conflicts

        # Find the correct category folder
        for category, folder_name in folder_map.items():
            if file.suffix in extensions.get(category, []):
                destination = recentlyDownloaded / folder_name
                break
        else:
            continue  # Skip files that don't match any category

        # Move file, renaming if necessary
        try:
            shutil.move(file, destination)
        except shutil.Error:
            new_name = f"{file.stem}_{renameTime}{file.suffix}"
            renamed_file = file.with_name(new_name)
            file.rename(renamed_file)  # Rename first
            shutil.move(renamed_file, destination)  # Move after renaming
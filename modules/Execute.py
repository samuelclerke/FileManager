import json
from pathlib import Path
import os
import shutil

class Execute:
  def __init__(self):
    pass

  def default(self):
    downloadsPath = Path.home() / "Downloads"
    documentsPath = Path.home() / "Documents"
    recentlyDownloaded = documentsPath / "Recently Downloaded"
    try:
      os.mkdir(recentlyDownloaded)
    except FileExistsError as e:
      print(f'Path already exists: {e}')

    folders = ['Images & Pictures', 'Music & Audio', 'Compressed & Zipped', 'Documents', 'Executables', 'Videos']

    for folder in folders:
      try:
        os.mkdir(recentlyDownloaded / folder)
      except FileExistsError as e:
        print(f'Path already exists: {e}')

    downloadsFiles = os.listdir(downloadsPath)
    executableExtensions = ('.apk', '.app', '.bat', '.bin', '.cmd', '.com', '.exe', '.ipa', '.jar', '.run', '.sh')
    compressedExtensions = ('.7z', '.cbr', '.deb', '.gz', '.pkg', '.rar','.rpm', '.tar.gz', '.xapk', '.zip', '.zipx', '.tgz', '.tar.xz', '.tar.bz2')
    imagesExtensions = ('.bmp', '.dcm', '.dds', '.djvu', '.gif', '.heic', '.jpg', '.png', '.psd', '.tga', '.tif', '.webp', '.ai', '.cdr', '.emf', '.eps', '.ps', '.sketch', '.svg', '.vsdx')
    videoExtensions = ('.3gp', '.asf', '.avi', '.flv', '.m4v', '.mov', '.mp4', '.mpg', '.srt', '.swf', '.ts', '.vob', '.mkv', '.webm')
    audioExtensions = ('.aif', '.flac', '.m3u', '.m4a', '.mid', '.mp3', '.ogg', '.wav', '.wma')
    documentExtensions = ('.doc', '.docx', '.eml', '.msg', '.odt', '.pages', '.rtf', '.tex', '.txt', '.wpd', '.pdf')

    for file in downloadsFiles:
      if file.endswith(executableExtensions):
        shutil.move(downloadsPath / file, recentlyDownloaded / 'Executables')
      elif file.endswith(compressedExtensions):
        shutil.move(downloadsPath / file, recentlyDownloaded / 'Compressed & Zipped')
      elif file.endswith(videoExtensions):
        shutil.move(downloadsPath / file, recentlyDownloaded / 'Videos')
      elif file.endswith(imagesExtensions):
        shutil.move(downloadsPath / file, recentlyDownloaded / 'Images & Pictures')
      elif file.endswith(documentExtensions):
        shutil.move(downloadsPath / file, recentlyDownloaded / 'Documents')
      elif file.endswith(audioExtensions):
        shutil.move(downloadsPath / file, recentlyDownloaded / 'Music & Audio')

  def userDefault(self):
    pass
import json
from pathlib import Path
import os
import shutil
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from modules.Handler import Handler
import time

flag_stop = False

class Execute:
  def __init__(self):
    self.modes = ['default', 'user']
    print('Modes:', self.modes)
    mode = input('Mode Select: ').strip().lower()

    if mode in self.modes:
      method_name = f"m_{mode}"  # Generate the method name
      if hasattr(self, method_name):  # Check if the method exists
        getattr(self, method_name)()  # Call the method dynamically
      else:
        print(f"Error: Method '{method_name}' not found.")
    else:
      print("Invalid mode selected.")

  def m_default(self):
    fileExtensions = {
      'executable' : ('.apk', '.app', '.bat', '.bin', '.cmd', '.com', '.exe', '.ipa', '.jar', '.run', '.sh'),
      'compressed' : ('.7z', '.cbr', '.deb', '.gz', '.pkg', '.rar','.rpm', '.tar.gz', '.xapk', '.zip', '.zipx', '.tgz', '.tar.xz', '.tar.bz2'),
      'image' : ('.bmp', '.dcm', '.dds', '.djvu', '.gif', '.heic', '.jpg', '.png', '.psd', '.tga', '.tif', '.webp', '.ai', '.cdr', '.emf', '.eps', '.ps', '.sketch', '.svg', '.vsdx'),
      'video' : ('.3gp', '.asf', '.avi', '.flv', '.m4v', '.mov', '.mp4', '.mpg', '.srt', '.swf', '.ts', '.vob', '.mkv', '.webm'),
      'audio' : ('.aif', '.flac', '.m3u', '.m4a', '.mid', '.mp3', '.ogg', '.wav', '.wma'),
      'document' : ('.doc', '.docx', '.eml', '.msg', '.odt', '.pages', '.rtf', '.tex', '.txt', '.wpd', '.pdf')
    }
    thread_downloadsWatch = threading.Thread(target=self.downloadsWatch(fileExtensions))
    thread_downloadsWatch.start()

    timeCount = 0
    while True:
      cmd = input('# ').strip().lower()
      if cmd == 'stop':
        return

  def m_user(self):
    print('User Mode Activated.')

  def downloadsWatch(self, extensions : map):
    path = Path.home() / "Downloads"
    event_handler = Handler(extensions)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

  def listen_downloadsDirProcessor(self):
    global flag_stop
    print("Type 'stop' to end process.")
    cmd = input('# ').strip().lower()
    if cmd == 'stop':
      flag_stop = True
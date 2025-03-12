import json
from pathlib import Path
from collections import Counter
import os
from colorama import Fore, Back, Style
from colorama import init
init()

class Setup:
  def __init__(self):
    settingsPath = Path('settings/default.cfg')
    userSettingsPath = Path('settings/user.cfg')

    if settingsPath.is_file() and not userSettingsPath.is_file(): # Check for default configuration
      with open('settings/default.cfg', 'r') as file:
        settings = json.load(file)
        print(Fore.BLACK+ f'~ Using {settingsPath}.' + Style.RESET_ALL)
      

    elif userSettingsPath.is_file():
      with open('settings/user.cfg', 'r') as file:
        settings = json.load(file)
        print(f'Using {userSettingsPath}.')

    else:
      settings = {
        'downloads' : {
          'path' :  str(Path.home() / "Downloads"),
          'sub_directories' : [
            'Executables',
            'Compressed',
            'Videos',
            'Images',
            'Documents',
            'Audio'
          ]
        }
      }
      os.makedirs('settings', exist_ok=True)

      with open('settings/default.cfg', 'x') as f:
        json.dump(settings, f, indent=2)



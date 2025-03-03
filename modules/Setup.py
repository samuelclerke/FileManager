import json
from pathlib import Path
from collections import Counter
import os
from colorama import Fore, Back, Style
from colorama import init
init()

class Setup:
  def __init__(self):
    try:
      with open('settings.cfg', 'r') as settings_file:  # This raises FileNotFoundError if the file is missing
        settings = json.load(settings_file)
        print("Config file loaded.")
      self.Setup()
        
    except FileNotFoundError as e: # No config file found so treat as first time setup and create file.
      print(f"Error finding config: {e}")
      settings = {
        'skipSetup' : False,
        'downloadsDirectories' : []
      }
      self.firstTimeSetup()
  

  # Initial Setup Process going over all features of the product. Should create the settings.cfg file at the end.
  def firstTimeSetup(self): 
    print(Fore.CYAN + "--(First Time Setup)--" + Style.RESET_ALL)
    while (1):
      download = input("Would you like to allow FileManager to organise your [Downloads] folder? (Y/n) ")
      if download.lower() == 'y':
        while (1):
          try:
              print('\nWhat folders would you like?')
              print('Images (1), Documents (2), Sounds (3), Executables (4), Compressed (5)')
              supports = list(map(int,(input('\nEnter a list of corresponding numbers seperated by spaces (eg. 1 3 5): ').split())))
              os.system('cls')
          except:
            os.system('cls')
            print(Fore.RED + "Invalid input. Follow instructions carefully." + Style.RESET_ALL)
          

        break
      elif download.lower() == 'n':
        break
      else: 
        os.system('cls')
        print(Fore.RED + "Invalid Input.\n\n" + Style.RESET_ALL)

  
  def Setup(self):
    print("--(Setup Process)--")
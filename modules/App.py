from modules.Setup import Setup
from modules.Execute import Execute
import sys
from colorama import Fore, Back, Style
from colorama import init
init()

class App:
  def __init__(self, option: str):
    option = option.lower()
    execute = Execute()
    
    match option:
      case 'setup':
        setup = Setup()
      case 'default': # Based on v0.1
        execute.default()
      case _:
        execute.userDefault()

def getArg() -> str:
  try: 
    opt = sys.argv[1]
  except :
    print(Fore.CYAN + "NOTICE: No arg parsed. Running USER_DEFAULT." + Style.RESET_ALL)
    opt = ''

  return opt
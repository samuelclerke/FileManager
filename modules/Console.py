import modules.Boxify as Boxify

class Console():
  def __init__(self):
    while True:
      cmd = input('# ').strip().lower()
      match cmd:
        case 'quit' | 'q':
          return
        case _:
          method = f"cmd_{cmd}"
  
  def cmd_help():

  def cmd_settings():
    pass
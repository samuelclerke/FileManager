from modules.Setup import Setup
from modules.Execute import Execute
import tracemalloc
import modules.Boxify as Boxify

class App:
  def __init__(self):
    tracemalloc.start()
    Boxify.printHeading('Initialising FileManager | Welcome to sophistication automated.')
    setup = Setup()
    execute = Execute()
        
    print(tracemalloc.get_traced_memory())
    tracemalloc.stop()
from modules.App import *

def main():
  tracemalloc.start()
  app = App()
  print(tracemalloc.get_traced_memory())
  tracemalloc.stop()

if __name__ == '__main__':
  main()
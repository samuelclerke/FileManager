from modules.App import *
import sys
import tracemalloc

def main():
  tracemalloc.start()
  opt = getArg()
  app = App(opt)
  print(tracemalloc.get_traced_memory())
  tracemalloc.stop()

if __name__ == '__main__':
  main()
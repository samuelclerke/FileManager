def printHeading(input : str):
  length = len(input)
  top = '┌' + ('─' * (length + 2)) + '┐'
  bottom = '└' + ('─' * (length + 2)) + '┘'
  print(top + '\n' + '│ ' + input + ' │' + '\n' + bottom)

if __name__ == '__main__':
  printHeading('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
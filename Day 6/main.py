def readFile(filename: str = 'input.txt') -> str:
  """
    read in input file
    Args:
        filename: filename to find

    Returns:
        str: txt from file
    """
  file = open(filename, "r")
  return file.read()


def parsePacket(input):
  #1034
  strInput = list(input)
  for i in range(3, len(strInput)):
    if len(set([strInput[ele] for ele in range(i - 3, i + 1)])) == 4:
      return i + 1
      
  return -1

def parsePacket14(input):
  strInput = list(input)
  for i in range(13, len(strInput)):
    #print([strInput[ele] for ele in range(i - 14, i, 1)])
    if len(set([strInput[ele] for ele in range(i - 13, i + 1)])) == 14:
      print([strInput[ele] for ele in range(i - 13, i + 1)])
      return i + 1
      
  return -1


def main():
  input = readFile('Day 6/input.txt')

  val = parsePacket14(input)

  print(val)


if __name__ == "__main__":
    main()

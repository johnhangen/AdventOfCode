########################################################################################################################
# Created by Jack Hangen
# Version 1
# advent calender of code
########################################################################################################################


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


def att1(input):
  count: int = 0
  
  for line in input.splitlines():
    spots = line.split(sep=',')

    spot0 = spots[0].split(sep='-')
    spot1 = spots[1].split(sep='-')

    if (spot0[0] <= spot1[0] and spot1[1] <= spot0[1]) or (spot1[0] <= spot0[0] and spot0[1] <= spot1[1]):
      #print(f"{spot0[0]} <= {spot1[0]} and {spot1[1]} <= {spot0[1]})")
      count = count + 1
    elif (spot0 == spot1):
      count = count + 1

  print(count)


def main():
  input = readFile('input.txt')

  att1(input) 
  

if __name__ == "__main__":
  main()

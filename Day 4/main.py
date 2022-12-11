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
  count = 0
  
  for line in input.splitlines():
    spots = line.split(sep=',')

    spot0 = spots[0].split(sep='-')
    spot1 = spots[1].split(sep='-')

    if (int(spot0[0]) <= int(spot1[0]) and int(spot0[1]) >= int(spot1[1])) or (int(spot1[0]) <= int(spot0[0]) and int(spot1[1]) >= int(spot0[1])):
      #print(f"{spot0[0]} <= {spot1[0]} and {spot1[1]} <= {spot0[1]})")
      count = count + 1

  print(count)

def att2(input):
  count = 0
  
  for line in input.splitlines():
    spots = line.split(sep=',')

    spot0 = spots[0].split(sep='-')
    spot1 = spots[1].split(sep='-')

      # (a_a <= b_a and a_b >= b_b) or (b_a <= a_a and b_b >= a_b)
    if max(int(spot0[0]), int(spot1[0])) <= min(int(spot0[1]), int(spot1[1])):
      count = count + 1

      # 780 too low
      # 971 too high

  print(count)

def main():
  input = readFile('Day 4/input.txt')

  att1(input) 
  att2(input)
  

if __name__ == "__main__":
  main()

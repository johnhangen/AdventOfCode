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

class Matrix:

  def __init__(self, size=1000) -> None:
     self.data = [['.' for x in range(size)] for x in range(size)]
     self.start = 500,500
     self.currH = 500,500
     self.currT = 500,500

  def printData(self):
    for x, line in enumerate(self.data):
      for y, char in enumerate(line):
        if y == self.currH[1] and x == self.currH[0]:
          print('H', end =' ')
        elif y == self.currT[1] and x == self.currT[0]:
          print('T', end =' ')
        elif y == self.start[1] and x == self.start[0]:
          print('S', end =' ')
        else:
          print('.', end =' ')
      print('\n')

  def printFinalData(self):
    for x, line in enumerate(self.data):
      for y, char in enumerate(line):
          print(self.data[x][y], end =' ')
      print('\n')

  def moveHead(self, dir):
    x, y = self.currH
    if dir == 'R':
      y = y + 1
    elif dir == 'L':
      y = y - 1
    elif dir == 'U':
      x = x - 1
    elif dir == 'D':
      x = x + 1
    else:
      print('invald input')

    self.currH = x, y

  def moveTail(self):
    # check if the H is close enough
    Hx, Hy = self.currH
    Tx, Ty = self.currT

    # if the head and tail aren't touching and aren't in the same row or column

    # need to check if they are touching
    if Hx != Tx and Hy != Ty and abs(Hx - Tx) > 1 or abs(Hy - Ty) > 1:
      if Hx > Tx and Hy > Ty:
        Tx = Tx + 1
        Ty = Ty + 1
      elif Hx < Tx and Hy > Ty:
        Tx = Tx - 1
        Ty = Ty + 1
      elif Hx < Tx and Hy < Ty:
        Tx = Tx - 1
        Ty = Ty - 1
      elif Hx > Tx and Hy < Ty:
        Tx = Tx + 1
        Ty = Ty - 1

    if Tx + 2 == Hx and Ty == Hy:
      Tx = Tx + 1
    elif Tx - 2 == Hx and Ty == Hy:
      Tx = Tx - 1
    elif Ty + 2 == Hy and Tx == Hx:
      Ty = Ty + 1
    elif Ty - 2 == Hy and Tx == Hx:
      Ty = Ty -1

    print(Tx, Ty)
    self.data[Tx][Ty] = '#'
    self.currT = Tx, Ty

  def countTpos(self) -> int:
      count = 0

      for x, line in enumerate(self.data):
        for y, char in enumerate(line):
          if self.data[x][y] == '#':
            count = count + 1

      return count
      

def main():
    input = readFile('Day 9/input.txt')

    matrix = Matrix()

    matrix.printData()

    for line in input.splitlines():
        dir, movement = line.split(' ')
        #print(f"== {dir} {movement} ==")
        for spots in range(int(movement)):
          matrix.moveHead(dir)
          matrix.moveTail()
          #matrix.printData()
          #print('\n')


    matrix.printFinalData()
    print(matrix.countTpos())
                

if __name__ == "__main__":
    main()
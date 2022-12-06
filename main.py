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


def calcScoreSecondcalcScore(input: str) -> int:
  runningTotal: int = 0
  dic = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6,
  }

  for line in input.splitlines():
    runningTotal = runningTotal + dic.get(line)

  return runningTotal


def calcScoreSecond(input: str) -> int:
  runningTotal: int = 0
  dic = {
    "A X": 3 + 0,
    "A Y": 1 + 3,
    "A Z": 2 + 6,
    "B X": 1 + 0,
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    "C X": 2 + 0,
    "C Y": 3 + 3,
    "C Z": 1 + 6,
  }

  for line in input.splitlines():
    runningTotal = runningTotal + dic.get(line)

  return runningTotal


def main():
  input = readFile('input.txt')

  print(calcScoreSecond(input))


if __name__ == "__main__":
  main()

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


def getPriority(list):
  returnVal = 0

  for i, diff in enumerate(list):
    if diff.isupper():
      returnVal = (ord(diff) - 38) + returnVal
    else:
      returnVal = (ord(diff) - 96) + returnVal

  return returnVal

def qu1(input):
  diffList = []

  for line in input.splitlines():
    str1 = line[:len(line) // 2]
    str2 = line[len(line) // 2:]

    for ele in str1:
      if ele in str2:
        #print(f"{str1}-{str2} = {ele}")
        diffList.append(ele)
        break

  return diffList

def qu2(input):
  diffList = []
  lines = input.splitlines()

  for i, line in enumerate(lines):
    if i%3 == 0:
      for ele in line:
        if ele in lines[i+1] and ele in lines[i+2]:
          #print(f"{lines[i]}, {lines[i+1]}, {lines[i+2]}, {ele}")
          diffList.append(ele)
          break

  return diffList


def main():
  input = readFile('input.txt')

  print(getPriority(qu1(input)))

  print(getPriority(qu2(input)))


if __name__ == "__main__":
  main()

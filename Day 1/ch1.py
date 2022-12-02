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


def calcMax(input:str) -> int:
    """
    finds out which elf is carrying the most
    Args:
        input: elf manifest

    Returns:
        int: total pounds
    """
    currMax = 0
    runningSum = 0

    for line in input.splitlines():
        if line == "":
            if runningSum > currMax:
                currMax = runningSum
            runningSum = 0
        else:
            runningSum = int(line) + runningSum

    return currMax


def calcMaxThree(input:str) -> int:
    """
    finds out which 3 elf is carrying the most
    Args:
        input: elf manifest

    Returns:
        int: total pounds for three elfs
    """
    currList = []
    runningSum = 0

    for line in input.splitlines():
        if line == "":
            currList.append(runningSum)
            runningSum = 0
        else:
            runningSum = int(line) + runningSum

    currList.sort()

    return currList[-1] + currList[-2] + currList[-3]

def main():
    input = readFile('Day 1\input.txt')
    
    print(f"The current max is {calcMax(input=input)} units ")

    print(f"The current max for three elfs {calcMaxThree(input=input)} units")

    
if __name__ == "__main__":
    main()

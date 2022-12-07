class Stack:

    def __init__(self):
        self.stack = [None for ele in range(100)]
        self.index = 0

    def push(self, item):
        self.stack[self.index] = item
        self.index = self.index + 1

    def pop(self):
        self.index = self.index - 1
        ele = self.stack[self.index]
        #self.stack[self.index] = None
        return ele

    def top(self):
        return self.stack[self.index]

    def isEmpty(self):
        return self.index == 0

    def isFull(self):
        return self.index == 20


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


def initStacks(initstr: list) -> list:
    """
    inits the stacks for a given load out
    Args:
        initstr: string at top of input.txt used to create stacks

    Returns:
        stacks: list of stacks that are init
    """
    stacks = [Stack(), Stack(), Stack(), Stack(), Stack(), Stack(), Stack(), Stack(), Stack()]
    
    for i in range(len(initstr) -1, -1, -1):
        strLine = list(initstr[i])
        for i, sline in enumerate(strLine):
            if i%4 == 0 and sline == '[':
                stacks[int(i/4)].push('[' + strLine[i+1] + ']')

    return stacks


def exInstuct(stacks: list, amount: str, stack1: str, stack2: str) -> list:
    """
    excutes one line of instruction
    Args:
        stacks: list of stacks
        amount: amount ordered to be transfered
        stack1: index of stack to be removed from
        stack2: index of stack to be moved to

    Returns:
        stacks: list of stacks that are init
    """
    for i in range(int(amount)):
        stacks[int(stack2) - 1].push(stacks[int(stack1) - 1].pop())

    return stacks


def exInstuct9001(stacks: list, amount: str, stack1: str, stack2: str) -> list:
    """
    excutes one line of instruction
    Args:
        stacks: list of stacks
        amount: amount ordered to be transfered
        stack1: index of stack to be removed from
        stack2: index of stack to be moved to

    Returns:
        stacks: list of stacks that are init
    """
    tempList = []
    for i in range(int(amount)):
        tempList.append(stacks[int(stack1) - 1].pop())

    for i in range(len(tempList) -1, -1, -1):
        stacks[int(stack2) - 1].push(tempList[i])

    return stacks


def returnTop(stacks):
    for i, stack in enumerate(stacks):
        print(f"{i +1} {stack.pop()}")


def main():
    input = readFile('Day 5\input.txt')

    # init stacks
    stacks = input.splitlines()[:9]
    stacks = initStacks(stacks)

    # run though instructions
    instuct = input.splitlines()[10:]
    for line in instuct:
        stacks = exInstuct9001(stacks, line.split(' ')[1], line.split(' ')[3], line.split(' ')[5])

    returnTop(stacks)


if __name__ == "__main__":
    main()

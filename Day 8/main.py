# this is an awful solution, would like to go back and fix it

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


def calcTreeVis(input):
    treeMatrix = input.splitlines()

    for i, line in enumerate(treeMatrix):
        treeMatrix[i] = list(line)

    visibleTrees = 0

    for x in range(1, len(treeMatrix) -1):
        for y in range(1, len(treeMatrix[x]) -1):
            currCount = False
            # up
            for up in range(x -1, -1, -1): 
                if treeMatrix[x][y] > treeMatrix[up][y]:
                    if up == 0:
                        visibleTrees += 1
                        currCount = True
                else:
                    break
            # down
            if not currCount:
                for down in range(x + 1, len(treeMatrix)): 
                    if treeMatrix[x][y] > treeMatrix[down][y]:
                        if down == len(treeMatrix) -1:
                            visibleTrees += 1
                            currCount = True
                    else:
                        break
            # left
            if not currCount:
                for left in range(y -1, -1, -1): 
                    if treeMatrix[x][y] > treeMatrix[x][left]:
                        if left == 0:
                            visibleTrees += 1
                            currCount = True
                    else:
                        break
            # right
            if not currCount:
                for right in range(y + 1, len(treeMatrix[x])): 
                    if treeMatrix[x][y] > treeMatrix[x][right]:
                        if right == len(treeMatrix) -1:
                            visibleTrees += 1
                    else:
                        break
    
    print(visibleTrees + len(treeMatrix)*2 + len(treeMatrix[1])*2 - 4)


def main():
    input = readFile('Day 8/input.txt')
    treeMatrix = input.splitlines()
    scores = []

    for i, line in enumerate(treeMatrix):
        treeMatrix[i] = list(line)

    for x in range(1, len(treeMatrix) -1):
        for y in range(1, len(treeMatrix[x]) -1):
            score = 0
            # up
            treeCount = 0
            for up in range(x -1, -1, -1): 
                if treeMatrix[x][y] > treeMatrix[up][y]:
                    treeCount += 1
                elif treeMatrix[x][y] <= treeMatrix[up][y]:
                    treeCount += 1
                    break
                else:
                    break
            score += treeCount

            #down
            treeCount = 0
            for down in range(x + 1, len(treeMatrix)): 
                if treeMatrix[x][y] > treeMatrix[down][y]:
                    treeCount += 1
                elif treeMatrix[x][y] <= treeMatrix[down][y]:
                    treeCount += 1
                    break
                else:
                    break
            score = score * treeCount

            # left
            treeCount = 0
            for left in range(y -1, -1, -1): 
                if treeMatrix[x][y] > treeMatrix[x][left]:
                    treeCount += 1
                elif treeMatrix[x][y] <= treeMatrix[x][left]:
                    treeCount += 1
                    break
                else:
                    break
            score = score * treeCount

            # right
            treeCount = 0
            for right in range(y + 1, len(treeMatrix[x])): 
                if treeMatrix[x][y] > treeMatrix[x][right]:
                    treeCount += 1
                elif treeMatrix[x][y] <= treeMatrix[x][right]:
                    treeCount += 1
                    break
                else:
                    break
            score = score * treeCount

            scores.append(score)

    print(max(scores))    


if __name__ == "__main__":
    main()
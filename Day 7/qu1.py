class tree:

    def __init__(self, name, dtype, parent, data = 0):
        self.name = name
        self.type = dtype
        self.parent = parent
        self.data = data
        self.children = []


    def root():
        # return true if root
        pass

    def GetParent(self):
        return self.parent

    def GetChild(self, name):
        for child in self.children:
            if child.name == name:
                print(child.name)
                return child

    def addChild(self, item):
        self.children.append(item)

    def setData(self, data):
        self.data = data

    def GetSumOfChildren(self, nums):
        count = 0
        for child in self.children:
            if child.type == 'dir':
                throw, nums = child.GetSumOfChildren(nums)
                child.setData(throw)
                nums.update({child: child.data})
            count = child.data + count
        return count, nums


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


def initFileStruct(input):
    read = 0
    rootNode = tree('/', 'dir', 'root')
    curr = rootNode
    count = 0

    for line in input.splitlines()[1:]:
        # cd down
        if line[0] == '$' and line.split(' ')[1] == 'cd' and line.split(' ')[2] != "..":
            read = 0
            count += 1
            for node in curr.children:
                if node.name == line.split(' ')[2]:
                    curr = node
        # cd up
        elif line[0] == '$' and line.split(' ')[1] == 'cd' and line.split(' ')[2] == "..":
            curr = curr.GetParent()
            read = 0
            count += 1
        # ls
        elif line[0] == '$' and line.split(' ')[1] == 'ls':
            read = 1
        # read into curr node
        elif (read):
            if line.split(' ')[0] == 'dir':
                curr.addChild(tree(line.split(' ')[1], 'dir', curr))
                count += 1
            else:
                # add file into dir
                curr.addChild(tree(line.split(' ')[1], 'file', curr, int(line.split(' ')[0])))
                count += 1
        else:
            print(line)

    return rootNode , count + 1


def main():
    # read and init
    input = readFile('Day 7\input.txt')
    base, max = initFileStruct(input)

    fileStuct = base
    count = 0
    # dict to store loc of tree object and the value stored
    nums = {}

    # run through the dirs and calc the sum
    while count < max:
        for i, node in enumerate(fileStuct.children):
            count += 1
            if node.type == 'dir':  
                fileStuct = node    
                node.setData(node.GetSumOfChildren(nums))


    total, nums = base.GetSumOfChildren(nums)

    # part 1
    fileSize = 0
    for i in nums:
        if nums.get(i) < 100000:
            fileSize += nums.get(i)
    print(f"total file size for files less than 100,000 is {fileSize}")
    
    # part 2
    filesLargeEnough = []
    for i in nums:
        if nums.get(i) > 5349983:
            filesLargeEnough.append(nums.get(i))

    
    print(f"the samllest file size that can be deleted is {min(filesLargeEnough)}")


if __name__ == "__main__":
    main()
    
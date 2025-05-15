# scan for numbers, if surrounding has symbol, add the number to total

symbol = ['*', '#', '%', '=', '-', '/', '$', '+', '@', '&']
numsIndex = []
wholeNums = []

def fileToList(file: str):
    f = open(file, "r")
    lis = []
    for line in f:
        lis.append(list(line.strip()))
    return lis

def isSymbol(char: chr):
    return char in symbol

def surHasSymbol(j, i, data):
    for row in range(j - 1, j + 2):
        if row in range(len(data)):
            for col in range(i - 1, i + 2):
                if col in range(len(data[row])) and not (row == j and col == i):
                    if isSymbol(data[row][col]):
                        return True
    return False

def getWholeNum(ind: list):
    row = ind[0]
    colLeft = colRight = ind[1]
    left = right = []
    while colLeft - 1 > -1 and data[row][colLeft - 1].isdigit():
        left.insert(0, [row, colLeft - 1])
        colLeft -= 1
    left.append(ind)
    while colRight + 1 < len(data[row]) and data[row][colRight + 1].isdigit():
        left.append([row, colRight + 1])
        colRight += 1
    wholeNums.append(left)
    print(left)

def delDup(ls: list):
    newLs = []
    for i in ls:
        if i not in newLs:
            newLs.append(i)
    return newLs

# algo starts here
data = fileToList("day3.txt")
print(data)

for j in range(len(data)):
    line = data[j]
    for i in range(len(line)):
        char = line[i]
        if char.isdigit() and surHasSymbol(j, i, data):
            print("yes", j, " ", i, " ", char)
            numsIndex.append([j, i])

print(numsIndex)
for i in range(len(numsIndex)):
    print(getWholeNum(numsIndex[i]))
print(wholeNums)
wholeNums = delDup(wholeNums)
print(wholeNums)
total = 0
for wholeNum in wholeNums:
    toAdd = ""
    for num in wholeNum:
        toAdd += data[num[0]][num[1]]
    total += int(toAdd)
print(total)

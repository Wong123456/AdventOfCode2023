# scan for numbers, if surrounding has symbol, add the number to total

symbol = ['*', '#', '%', '=', '-', '/', '$', '+', '@', '&']
numssurNumsex = []
wholeNums = []

def fileToList(file: str):
    f = open(file, "r")
    lis = []
    for line in f:
        lis.append(list(line.strip()))
    return lis

def isSymbol(char: chr):
    return char in symbol

def getSurrounding(j, i, data):
    re = []
    for row in range(j - 1, j + 2):
        if row in range(len(data)):
            for col in range(i - 1, i + 2):
                if col in range(len(data[row])) and not (row == j and col == i) and data[row][col].isdigit():
                    re.append([row, col])
    return re

def getRatio(surNums: list):
    ratio = 0
    wholeNumIdxs = []
    for digitIdx in surNums:
        print(digitIdx)
        row = digitIdx[0]
        colLeft = colRight = digitIdx[1]
        wholeNumIdx = []
        while colLeft - 1 > -1 and data[row][colLeft - 1].isdigit():
            wholeNumIdx.insert(0, [row, colLeft - 1])
            colLeft -= 1
        wholeNumIdx.append(digitIdx)
        while colRight + 1 < len(data[row]) and data[row][colRight + 1].isdigit():
            wholeNumIdx.append([row, colRight + 1])
            colRight += 1
        wholeNumIdxs.append(wholeNumIdx)    
    wholeNumIdxs = delDup(wholeNumIdxs)
    print(wholeNumIdxs)
    if len(wholeNumIdxs) == 2:
        ratio = 1
        for wholeNum in wholeNumIdxs:
            num = ""
            for digIdx in wholeNum:
                num += data[digIdx[0]][digIdx[1]]
            ratio *= int(num)
    return ratio
        

def delDup(ls: list):
    newLs = []
    for i in ls:
        if i not in newLs:
            newLs.append(i)
    return newLs

# algo starts here
data = fileToList("day3.txt")
total = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        if (isSymbol(data[i][j])):
            surNums = getSurrounding(i, j, data)
            print("surNums: ", surNums)
            if (len(surNums) >= 2):
                total += getRatio(surNums)
print(total)
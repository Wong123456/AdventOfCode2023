import sys
sys.setrecursionlimit(10**7)
def getData(filePath: str):
    data = []
    f = open(filePath, "r")
    for line in f:
        line = line.strip().split(":")
        line = line[1].split("|")
        data.append([line[0].split(), line[1].split()])
    return data

def getMatchNo(winning, have):
    point = 0
    for nums in have:
        if nums in winning:
            point += 1
    return point

def getAllCards(idx):
    if idx >= len(totalCards): return
    cardNo = totalCards[idx]
    point = getMatchNo(data[cardNo - 1][0], data[cardNo - 1][1])
    copies = [int(cardNo + n + 1) for n in range(point)]
    totalCards[idx + 1: idx + 1] = copies
    getAllCards(idx + 1)

total = 0
data = getData("day4.txt")
totalCards = [int(n + 1) for n in range(len(data))]
getAllCards(0)
print(len(totalCards))
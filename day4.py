def getData(filePath: str):
    data = []
    f = open(filePath, "r")
    for line in f:
        line = line.strip().split(":")
        line = line[1].split("|")
        data.append([line[0].split(), line[1].split()])
    return data

total = 0
data = getData("day4.txt")
for entr in data:
    winning = entr[0]
    have = entr[1]
    
    point = 0
    for nums in have: 
        if nums in winning:
            if point == 0: point = 1
            else: point *= 2
    print(point)
    total += point
print(total)
from time import perf_counter
from copy import deepcopy
t1 = perf_counter()
def rowToExpand(data: list[list]):
    rowIdxs = []
    for rowIdx in range(len(data)):
        if all(c == "." for c in data[rowIdx]): rowIdxs.append(rowIdx)
    return rowIdxs

def colToExpand(data: list[list]):
    colIdxs = []
    for colIdx in range(len(data[0])):
        if all(c == "." for c in [data[r][colIdx] for r in range(len(data))]): colIdxs.append(colIdx)
    return colIdxs

def galaxiesPos(data: list[list]):
    galaxies = []
    for r in range(len(data)):
        for c in range(len(data[r])):
            if data[r][c] == "#": galaxies.append([r, c])
    return galaxies

def calSteps(x, y): return abs(x[0] - y[0]) + abs(x[1] - y[1])

def calSteps2(x, y, rows, cols, expansion):
    gal_rows, gal_cols, newRows, newCols = sorted([x[0], y[0]]), sorted([x[1], y[1]]), [], []
    newRows = [r for r in rows if gal_rows[0] < r < gal_rows[1]]
    newCols = [c for c in cols if gal_cols[0] < c < gal_cols[1]]
    return (gal_rows[1] - gal_rows[0] - len(newRows) + len(newRows)*expansion) + \
        (gal_cols[1] - gal_cols[0] - len(newCols) + len(newCols)*expansion)

with open("day11.txt", "r") as f:
    data = [[c for c in l] for l in f.read().split("\n")]
    data2 = deepcopy(data)
    rowAdd = colAdd = 0
    for row in rowToExpand(data):
        data.insert(row + rowAdd, ["."]*(len(data[0])))
        rowAdd += 1
    for col in colToExpand(data):
        for line in data:
            line.insert(col + colAdd, ".")
        colAdd += 1
    galaxies1, galaxies2, total1, total2 = galaxiesPos(data), galaxiesPos(data2), 0, 0
    for i in range(len(galaxies1)):
        for n in galaxies1[i + 1::]:
            total1 += calSteps(galaxies1[i], n)
    print("Part 1: ", total1)

    rows, cols, expansion = rowToExpand(data2), colToExpand(data2), 1000000
    for i in range(len(galaxies2)):
        for n in galaxies2[i + 1::]:
            total2 += calSteps2(galaxies2[i], n, rows, cols, expansion)
    print("Part 2: ", total2)
print(perf_counter() - t1)
        
from time import perf_counter
import numpy as np
t1 = perf_counter()

def inRange(ptr: dict):
    for i in ptr.values():
        if i < -1 or i >= len(maze): return False
    return True

def canMoveUp(up, curr):
    if (up == "|" or up == "7" or up == "F" or up == "S") and (curr == "|" or curr == "L" or curr == "J"): return True


def getSurr(ptr: dict, prevPtr: dict):
    # print("ptr in getSurr: " , ptr)
    # print("prev in getSurr: ", prevPtr)
    curr = maze[ptr["row"]][ptr["col"]]
    surr = {}
    upPtr = {**ptr, "row": ptr["row"] - 1}
    if upPtr != prevPtr and inRange(upPtr):
        up = maze[upPtr["row"]][upPtr["col"]]
        if (up == "|" or up == "7" or up == "F" or up == "S") and (curr == "|" or curr == "L" or curr == "J" or curr == "S"):
            surr.update({"up": upPtr})

    downPtr = {**ptr, "row": ptr["row"] + 1}
    if downPtr != prevPtr and inRange(downPtr):
        down = maze[downPtr["row"]][downPtr["col"]]
        if (down == "|" or down == "L" or down == "J" or down == "S") and (curr == "F" or curr == "7" or curr == "|" or curr == "S"):
            surr.update({"down": downPtr})
    
    leftPtr = {**ptr, "col": ptr["col"] - 1}
    if leftPtr != prevPtr and inRange(leftPtr):
        left = maze[leftPtr["row"]][leftPtr["col"]]
        if (left == "-" or left == "L" or left == "F" or left == "S") and (curr == "-" or curr == "7" or curr == "J" or curr == "S"):
            surr.update({"left": leftPtr})
    
    rightPtr = {**ptr, "col": ptr["col"] + 1}
    if rightPtr != prevPtr and inRange(rightPtr):
        right = maze[rightPtr["row"]][rightPtr["col"]]
        if (right == "-" or right == "7" or right == "J" or right == "S") and (curr == "-" or curr == "L" or curr == "F" or curr == "S"):
            surr.update({"right": rightPtr})
    return surr

def move(node: dict, prevPtr):
    direction, currPtr = list(node.items())[0]
    return getSurr(currPtr, prevPtr)

ptr = {"row": -1, "col": -1}
with open("day10.txt", "r") as f:
    maze = [[c for c in l] for l in f.read().split("\n")]
    start = leftprev = rightprev = dict(ptr)
    start["row"], start["col"] = list(map(int, np.argwhere(np.array(maze) == "S").tolist()[0]))
    startItems = getSurr(start, leftprev)
    # print("Start: ", startItems)
    it = list(startItems.items())
    left, right = {it[0][0]: it[0][1]}, {it[1][0]: it[1][1]}
    leftCount = rightCount = 1

    # print(list(left.values())[0])
    while list(left.values())[0] != list(right.values())[0]:
        # print("left: ", list(left.values())[0], "right: ", list(right.values())[0])
        temp = list(left.values())[0]
        left = move(left, leftprev)
        leftprev = temp
        leftCount += 1
        if list(left.values())[0] != list(right.values())[0]:
            temp = list(right.values())[0]
            right = move(right, rightprev)
            rightprev = temp
            # rightCount += 1
        # print("new left", left, leftCount, "new right", right, rightCount, "\n")
    print(leftCount)



print(perf_counter() - t1)

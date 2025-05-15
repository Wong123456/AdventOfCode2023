import numpy as np
from time import perf_counter
t1 = perf_counter()
f = open("day8.txt", "r")
file = f.read().split("\n")
currNodes, endSteps, steps, directions, toPop = [], [], 0, file[0].strip(), -1

nodesDict = {}
for node in file[2:]:
    node = node.split(" = ")
    nodesDict.update({node[0]: node[1][1:-1].split(", ")})
    if node[0].endswith("A"): currNodes.append(node[0])

while len(currNodes) > 0:
    if toPop > -1:
        currNodes.pop(toPop)
        toPop = -1
    direction = directions[steps % len(directions)]
    for ind, currNode in enumerate(currNodes):
        if currNode.endswith("Z"):
            endSteps.append(steps)
            toPop = ind
        else:
            left, right = nodesDict[currNode]
            if direction == "L": currNodes[ind] = left
            elif direction == "R": currNodes[ind] = right
    steps += 1
print(np.lcm.reduce(endSteps))
print(perf_counter() - t1)
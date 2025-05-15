f = open("day8.txt", "r")
file = f.read().split("\n")

nodesDict = {}
for node in file[2:]:
    node = node.split(" = ")
    nodesDict.update({node[0]: node[1][1:-1].split(", ")})

currNode, steps, directions = nodesDict["AAA"], 0, file[0].strip()
while currNode != nodesDict["ZZZ"]:
    direction = directions[steps % len(directions)]
    left, right = currNode
    if direction == "L": currNode = nodesDict[left]
    else: currNode = nodesDict[right]
    steps += 1
print(steps)
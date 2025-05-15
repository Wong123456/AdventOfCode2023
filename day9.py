from time import perf_counter
t1 = perf_counter()
def findFuture(history: list):
    if all( history[-1][i + 2] - history[-1][i + 1] == history[-1][i + 1] - history[-1][i] for i in range(len(history[-1]) - 2) ):
        history[-1].append(history[-1][-1] + history[-1][1] - history[-1][0])
        return calFuture(history, len(history) - 1)
    history.append([history[-1][i + 1] - history[-1][i] for i in range(len(history[-1]) - 1)])

    return findFuture(history)

def calFuture(history: list, ind: int):
    if ind == 0 or len(history) == 0: return history[0][-1]
    history[ind - 1].append(history[ind][-1] + history[ind - 1][-1])
    return calFuture(history, ind - 1)

total = total2 = 0
with open("day9.txt", "r") as f:
    histories = f.read().split("\n")
    for history in histories:
        history = [int(x) for x in history.split()]
        total += findFuture([history])
        total2 += findFuture([list(reversed(history))])
print(total, total2)
print(perf_counter() - t1)
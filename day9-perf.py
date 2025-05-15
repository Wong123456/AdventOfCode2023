from time import perf_counter
t1 = perf_counter()
# def findFuture(history: list):
#     if all( history[-1][i + 2] - history[-1][i + 1] == history[-1][i + 1] - history[-1][i] for i in range(len(history[-1]) - 2) ):
#         return calFuture(history, len(history) - 1)
#     history.append([history[-1][i + 1] - history[-1][i] for i in range(len(history[-1]) - 1)])

#     return findFuture(history)

def findFuture(history: list):
    while not all( history[-1][i + 2] - history[-1][i + 1] == history[-1][i + 1] - history[-1][i] for i in range(len(history[-1]) - 2) ):
        history.append([history[-1][i + 1] - history[-1][i] for i in range(len(history[-1]) - 1)])
    return calFuture(history, len(history) - 1)


# def calFuture(history: list, ind: int):
#     ftr = history[-1][-1] + history[-1][1] - history[-1][0]
#     def calFutureFrmBottom(ind):
#         nonlocal ftr
#         if ind == 0: return ftr
#         ftr += history[ind - 1][-1]
#         return calFutureFrmBottom(ind - 1)
#     if len(history) == 0: return ftr
#     else: return calFutureFrmBottom(ind)

def calFuture(history: list, ind: int):
    ftr = history[-1][-1] + history[-1][1] - history[-1][0]
    if len(history) > 0:
        while ind > 0:
            ftr += history[ind - 1][-1]
            ind -= 1
    return ftr

total = total2 = 0
with open("day9.txt", "r") as f:
    histories = f.read().split("\n")
    for history in histories:
        history = [int(x) for x in history.split()]
        total += findFuture([history])
        total2 += findFuture([list(reversed(history))])
print(total, total2)
print(perf_counter() - t1)
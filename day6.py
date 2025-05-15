from time import perf_counter
f = open("day6.txt")
t1 = perf_counter()

times = distances = []
for line in f: 
    if line.startswith("Time:"):
        times = list(map(int, line.strip().split(":")[1].split()))
    if line.startswith("Distance:"):
        distances = list(map(int, line.strip().split(":")[1].split()))

total = 1
for i in range(len(times)):
    time, distance = times[i], distances[i]
    winCount = 0
    for i in range(time + 1):
        if i * (time - i) > distance: winCount += 1
    total *= winCount
print(total)

t2 = perf_counter()
print(t2 - t1)
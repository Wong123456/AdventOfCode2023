from math import sqrt, ceil, floor
from time import perf_counter
t1 = perf_counter()
f = open("day6.txt")
for line in f: 
    if line.startswith("Time:"):
        time = int("".join(line.strip().split(":")[1].split()))
    if line.startswith("Distance:"):
        distance = int("".join(line.strip().split(":")[1].split()))

print(time, distance)
# total = 1
# winCount = 0
# for i in range(time + 1):
#     if i * (time - i) > distance: winCount += 1
# total *= winCount
# print(total)

a, b, c = 1, -time, distance
min = ceil((-b - sqrt(b**2 - 4*a*c)) / 2*a)
max = floor((-b + sqrt(b**2 - 4*a*c)) / 2*a)
print(max - min + 1)
t2 = perf_counter()
print(t2 - t1)


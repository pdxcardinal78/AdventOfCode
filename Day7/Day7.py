import statistics
import math

with open("AOC_Day7.txt", "r") as day7:
    crabs = day7.readlines()

crabs = [int(x) for x in crabs[0].split(',')]


# Mode is too high 479517
# mode = statistics.mode(crabs)

median = statistics.median(crabs)
delta_median= [abs(x-median) for x in crabs]

print(sum(delta_median))


# Part 2
avg = math.floor(statistics.mean(crabs))


delta_avg = 0

for x in crabs:
    for i in range(1, abs(x-avg)+1):
        delta_avg+=i

print(delta_avg)


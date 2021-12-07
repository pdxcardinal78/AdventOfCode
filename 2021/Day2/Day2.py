# Part 1

with open("AOC_Day2.txt", "r") as day2:
    movements = day2.readlines()

movements_clean = [x.split("\n")[0] for x in movements]
move_tup = [x.split(" ") for x in movements_clean]

forward = 0
depth = 0
aim = 0
forward2 = 0
depth2 = 0

for i in move_tup:
    if i[0] == "forward":
        forward += int(i[1])
    elif i[0] == "down":
        depth += int(i[1])
    elif i[0] == "up":
        depth -= int(i[1])

print(f"Forward:{forward} \nDepth:{depth}\nMath:{forward*depth}")

# Part 2

for i in move_tup:
    if i[0] == "forward":
        forward2 += int(i[1])
        depth2 += aim * int(i[1])
    elif i[0] == "down":
        aim += int(i[1])
    elif i[0] == "up":
        aim -= int(i[1])

print(f"Forward:{forward2} \nDepth:{depth2}\nMath:{forward2*depth2}")

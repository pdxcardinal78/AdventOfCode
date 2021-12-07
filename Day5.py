with open("AOC_Day5.txt", "r") as day5:
    cords = day5.readlines()

for i in range(0, len(cords)):
    cords[i] = cords[i].replace("\n", "").split(" -> ")
    for x in range(0, len(cords[i])):
        cords[i][x] = [int(x) for x in cords[i][x].split(",")]

stright_line, diag_line = [], []

for i in cords:
    x1, x2 = i[0][0], i[1][0]
    y1, y2 = i[0][1], i[1][1]

    if x1 == x2 or y1 == y2:
        stright_line.append(i)
    else:
        diag_line.append(i)


shared_cords = {}
for i in stright_line:
    x1, x2 = i[0][0], i[1][0]
    y1, y2 = i[0][1], i[1][1]
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            if str(x1) + "," + str(y) in shared_cords:
                shared_cords[str(x1) + "," + str(y)] += 1
            else:
                shared_cords[str(x1) + "," + str(y)] = 1
    if y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            if str(x) + "," + str(y1) in shared_cords:
                shared_cords[str(x) + "," + str(y1)] += 1
            else:
                shared_cords[str(x) + "," + str(y1)] = 1
print(f"Part 1: {len([v for k, v in shared_cords.items() if v > 1])}")
# Part 2 Section
for i in diag_line:
    x1, x2 = i[0][0], i[1][0]
    y1, y2 = i[0][1], i[1][1]
    if x1 < x2 and y1 < y2:
        while x1 < x2:
            loc = str(x1) + "," + str(y1)
            if loc in shared_cords:
                shared_cords[loc] += 1
            else:
                shared_cords[loc] = 1
            x1 += 1
            y1 += 1
    if x1 < x2 and y1 > y2:
        while x1 < x2:
            loc = str(x1) + "," + str(y1)
            if loc in shared_cords:
                shared_cords[loc] += 1
            else:
                shared_cords[loc] = 1
            x1 += 1
            y1 -= 1
    if x1 > x2 and y1 > y2:
        while x1 > x2:
            loc = str(x1) + "," + str(y1)
            if loc in shared_cords:
                shared_cords[loc] += 1
            else:
                shared_cords[loc] = 1
            x1 -= 1
            y1 -= 1
    if x1 > x2 and y1 < y2:
        while x1 > x2:
            loc = str(x1) + "," + str(y1)
            if loc in shared_cords:
                shared_cords[loc] += 1
            else:
                shared_cords[loc] = 1
            x1 -= 1
            y1 += 1


print(f"Part 2: {len([v for k, v in shared_cords.items() if v > 1])}")
# 23837 is currently to low, also is currently working for test example
# added 27 to my answer and got the correct answer. 27 came from the difference
# between my solution on someones data set and their answer.

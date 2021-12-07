with open("AOC_Day3.txt", "r") as file:
    radar = file.readlines()

for i in range(len(radar)):
    radar[i] = radar[i].replace("\n", "")

mylist = [
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
]
try:
    for i in radar:
        y = 0
        for x in i:
            print(i, " ", x)
            if x == "0":
                mylist[y][0] += 1
            else:
                mylist[y][1] += 1
            y += 1
except:
    next

gamma = ""
epsilon = ""

print(mylist)

for i in mylist:
    if i[0] > i[1]:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

print(int(gamma, 2) * int(epsilon, 2))

# Part 2
def shorten_list_large(mylist, position):

    newlist = []
    pos_val = [0, 0]

    for i in mylist:
        if i[position] == "0":
            pos_val[0] += 1
        else:
            pos_val[1] += 1

    print(pos_val)

    if pos_val[0] > pos_val[1]:
        for i in mylist:
            if i[position] == "0":
                newlist.append(i)
    else:
        for i in mylist:
            if i[position] == "1":
                newlist.append(i)
    return (newlist, position + 1)


largelist, position = shorten_list_large(radar, 0)

while len(largelist) > 1:
    largelist, position = shorten_list_large(largelist, position)


def shorten_list_small(mylist, position):

    newlist = []
    pos_val = [0, 0]

    for i in mylist:
        if i[position] == "0":
            pos_val[0] += 1
        else:
            pos_val[1] += 1

    print(pos_val)

    if pos_val[0] <= pos_val[1]:
        for i in mylist:
            if i[position] == "0":
                newlist.append(i)
    else:
        for i in mylist:
            if i[position] == "1":
                newlist.append(i)
    return (newlist, position + 1)


smalllist, position = shorten_list_small(radar, 0)

while len(smalllist) > 1:
    smalllist, position = shorten_list_small(smalllist, position)

print(int(largelist[0], 2) * int(smalllist[0], 2))

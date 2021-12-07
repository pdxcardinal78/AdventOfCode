with open("AOC_Day6.txt", "r") as day6:
    lanter_fish = day6.readlines()
lanter_fish = [int(x) for x in lanter_fish[0].split(",")]


def day_tick(population):
    lanter_fish_2 = []

    for i in population:
        if i == 0:
            lanter_fish_2.append(6)
            lanter_fish_2.append(8)
        else:
            lanter_fish_2.append(i - 1)

    return lanter_fish_2


# Part 1
lanter_fish_1 = lanter_fish
# for i in range(0, 80):
#     lanter_fish_1 = day_tick(lanter_fish_1)

# print(len(lanter_fish_1))

# Part 2


def convert_to_dict(fishlist):
    fish_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

    for i in fishlist:
        fish_dict[i] += 1

    return fish_dict


def day_tick_dict(fish_dict):
    new_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    for key in fish_dict:
        if key == 0:
            new_dict[8] += fish_dict[0]
            new_dict[6] += fish_dict[0]
        else:
            new_dict[key - 1] += fish_dict[key]

    return new_dict


fish_dict = convert_to_dict(lanter_fish)

for i in range(256):
    fish_dict = day_tick_dict(fish_dict)

print(sum(fish_dict.values()))

fish_dict_1 = convert_to_dict(lanter_fish_1)
for i in range(80):
    fish_dict_1 = day_tick_dict(fish_dict_1)
print(sum(fish_dict_1.values()))

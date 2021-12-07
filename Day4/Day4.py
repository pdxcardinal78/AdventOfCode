with open("AOC_Day4.txt", "r") as day4:
    bingo_data = day4.readlines()

bingo_numbers = bingo_data[0].split(",")
bingo_numbers = [int(x) for x in bingo_numbers]

bingo_cards = []

bingo_data = bingo_data[2:]

x = 0
while x < 599:
    bingo_cards.append(bingo_data[x : x + 5])
    x += 6

for i in range(0, len(bingo_cards)):
    y = []
    for x in bingo_cards[i]:
        z = x.replace("\n", "").split(" ")
        d = {}
        for n in z:
            if n == "":
                next
            else:
                d[int(n)] = 0
        y.append(d)
    bingo_cards[i] = y

# print(bingo_cards[0])


def call_number(card, number):

    for row in card:
        if number in row:
            row[number] = 1

    return card


def check_bingo(card):
    for i in card:
        if sum(i.values()) == 5:
            total = 0
            for t in card:
                total += sum([k for k, v in t.items() if v == 0])
            return total
    for i in range(0, 5):
        col = 0
        for row in card:
            if row[list(row.keys())[i]] == 1:
                col += 1
        if col == 5:
            total = 0
            for t in card:
                total += sum([k for k, v in t.items() if v == 0])
            return total


def bingo():
    pulled_numbers = 0
    for num in bingo_numbers:
        pulled_numbers += 1
        for i in range(0, len(bingo_cards)):
            bingo_cards[i] = call_number(bingo_cards[i], num)
            if pulled_numbers > 5:
                card_total = check_bingo(bingo_cards[i])
                if card_total != None:
                    return print(
                        f"Card_Value={card_total}, Last_called={num}, Total = {card_total * num}, {pulled_numbers}"
                    )


def bingo_2():
    pulled_numbers = 0
    cards = {}
    for num in bingo_numbers:
        pulled_numbers += 1
        for i in range(0, len(bingo_cards)):
            bingo_cards[i] = call_number(bingo_cards[i], num)
            if pulled_numbers > 5:
                card_total = check_bingo(bingo_cards[i])
                if card_total != None:
                    if i in cards.keys():
                        next
                    else:
                        cards[i] = card_total * num
    return cards


print(bingo_2())

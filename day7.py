from operator import *
cardPowerDict = {"2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8, "T": 9, "J": 10, "Q": 11, "K": 12, "A": 13}

handDict = {"2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "T": 0, "J": 0, "Q": 0, "K": 0, "A": 0}

# game list [[cards, bid, power], [cards, bid, power]] then sort by its power, lowest rank has lowert power, rank = index of list + 1
#total += rank * bid

def sortHand(hand: list):
    sortedHand = sorted(hand, key=lambda card: cardPowerDict[card], reverse=True)
    return sortedHand

def getPower(hand: list):
    cardCount, power = dict(handDict), 0
    for card in hand: cardCount[card] += 1
    if 5 in cardCount.values(): power = 7
    elif 4 in cardCount.values(): power = 6
    elif 3 in cardCount.values(): 
        if 2 in cardCount.values(): power = 5
        else: power = 4
    elif 2 in cardCount.values(): 
        if countOf(cardCount.values(), 2) == 2: 
            power = 3
        else: power = 2
    elif 1 in cardCount.values(): power = 1
    return power

game = []
f = open("day7.txt", "r")
for line in f: 
    card, bid = line.split()
    power = getPower(card)
    game.append([card, int(bid), power])
game.sort(key=lambda hand:(hand[2], cardPowerDict[hand[0][0]], cardPowerDict[hand[0][1]], cardPowerDict[hand[0][2]]
                                    , cardPowerDict[hand[0][3]], cardPowerDict[hand[0][4]]))
total = 0
for hand in range(len(game)):
    print(game[hand])
    total += (hand + 1) * game[hand][1]
print(total)
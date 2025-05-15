from operator import *
cardPowerDict = {"J": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "Q": 11, "K": 12, "A": 13}

handDict = {"2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "T": 0, "J": 0, "Q": 0, "K": 0, "A": 0}

# game list [[cards, bid, power], [cards, bid, power]] then sort by its power, lowest rank has lowert power, rank = index of list + 1
#total += rank * bid

def sortHand(hand: list):
    sortedHand = sorted(hand, key=lambda card: cardPowerDict[card], reverse=True)
    return sortedHand

def getMaxCard(cardCount: dict):
    highestCardCount = max(cardCount.values())
    for sign, count in cardCount.items():
        if count == highestCardCount: return sign

def getPower(hand: list):
    cardCount, power = dict(handDict), 0
    for card in hand: cardCount[card] += 1
    highestCard, jCount = getMaxCard(cardCount), cardCount["J"]
    if highestCard == "J":
        cardCount["J"] = 0
    cardCount[getMaxCard(cardCount)] += jCount

    if 5 in cardCount.values(): power = 5
    elif 4 in cardCount.values(): power = 4
    elif 3 in cardCount.values(): 
        if 2 in cardCount.values(): power = 3.5
        else: power = 3
    elif 2 in cardCount.values(): 
        if countOf(cardCount.values(), 2) == 2: 
            power = 2.5
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
    # print(game[hand])
    total += (hand + 1) * game[hand][1]
print(total)
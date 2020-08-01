import random
from card import Card


class PokerUtils:
    cardColors = ["clubs", "diamonds", "hearts", "spades"]
    cardValues = range(2, 15)

    # provide every possible hand
    @staticmethod
    def getallhands():
        winhandlength = 5

        # name, rating, __cards
        # create royal flush
        winhands = []

        # create straight flush & royal flush
        basescore = 9
        for color in PokerUtils.cardColors:
            for i in PokerUtils.cardValues[0:-(winhandlength-2)]:
                handname = "straight flush "
                if i > 10:
                    handname = "royal flush "

                winhands.append([handname + color, basescore + (i - 2) / len(PokerUtils.cardValues[0:-(winhandlength-2)]), Card(color, i), Card(color, i+1), Card(color, i+2), Card(color, i+3), Card(color, i+4)])

        # create four of a kind
        basescore = 8
        handname = "four of a kind"
        for i in PokerUtils.cardValues:
            for j in range(0, 12):
                for fifthcolor in PokerUtils.cardColors:

                    fifthvalue = i + 1 + j

                    if fifthvalue == 15:
                        fifthvalue = 2
                    elif fifthvalue == 16:
                        fifthvalue = 3
                    elif fifthvalue > 16:
                        fifthvalue = fifthvalue - 13

                    # 2 conditions for 5th value: never be above 14 and never be the same as i
                    winhands.append(
                        [handname, basescore + (i - 2) / len(PokerUtils.cardValues), Card(PokerUtils.cardColors[0], i),
                         Card(PokerUtils.cardColors[1], i), Card(PokerUtils.cardColors[2], i),
                         Card(PokerUtils.cardColors[3], i), Card(fifthcolor, fifthvalue)])

        return winhands

    @staticmethod
    def getcardname(card):
        cardName = card.color
        if card.value == 2:
            return cardName + " 2"
        elif card.value == 3:
            return cardName + " 3"
        elif card.value == 4:
            return cardName + " 4"
        elif card.value == 5:
            return cardName + " 5"
        elif card.value == 6:
            return cardName + " 6"
        elif card.value == 7:
            return cardName + " 7"
        elif card.value == 8:
            return cardName + " 8"
        elif card.value == 9:
            return cardName + " 9"
        elif card.value == 10:
            return cardName + " 10"
        elif card.value == 11:
            return cardName + " Jack"
        elif card.value == 12:
            return cardName + " Queen"
        elif card.value == 13:
            return cardName + " King"
        elif card.value == 14:
            return cardName + " Ace"

    @staticmethod
    def createdeck():
        deck = []
        # init the 52 __cards
        for color in PokerUtils.cardColors:
            for value in PokerUtils.cardValues:
                deck.append(Card(color, value))
        random.shuffle(deck)
        return deck

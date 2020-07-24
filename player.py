from pokerUtils import PokerUtils
from card import Card


class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def draw(self, deck):
        self.cards.append(deck[0])
        print(self.name + " draws\t" + PokerUtils.getcardname(deck[0]))
        deck.pop(0)
        return deck

    def decide(self):
        return 1

    def gethandranking(self, communitycards):
        mycards = self.cards + communitycards

        print(mycards)
        samecolor = False
        if sum(mycard.color == "clubs" for mycard in mycards) >= 5 or sum(mycard.color == "diamonds" for mycard in mycards) >= 5 or sum(mycard.color == "hearts" for mycard in mycards) >= 5 or sum(mycard.color == "spades" for mycard in mycards) >= 5:
            samecolor = True

        # test shit
        mycards = [Card("clubs", 10), Card("clubs", 11), Card("clubs", 12), Card("clubs", 13), Card("clubs", 14)]
        winprobs = []
        for i in PokerUtils.getallhands():
            winprobs.append([i[1], self.comparehands(mycards, i[2:])])

        print()
        # calc how close to which one
        # get list with all poker hand rankings and closeness like (10, "Royal Flush", 0.8,),(9, "Straight Flush", 0),

        #
        # = set(mycards) & set(somehandranking)


    def comparehands(self, hand, targethand):
        score = 0
        for targetcard in targethand:
            for mycard in hand:
                if mycard.color == targetcard.color and mycard.value == targetcard.value:
                    score = score + 1
                    # remove these from the loop
                    hand.remove(mycard)
        if score > 0:
            score = score / len(targethand)
        return score

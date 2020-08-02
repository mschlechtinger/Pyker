from pokerUtils import PokerUtils
from card import Card


class Player:
    hasCalled = False

    def __init__(self, name, ishuman, chips):
        self.name = name
        self.isHuman = ishuman
        self.chips = chips
        self.__cards = []

    def draw(self, deck):
        self.__cards.append(deck[0])
        print(self.name + " draws\t" + PokerUtils.getcardname(deck[0]))
        deck.pop(0)

    def getname(self):
        return self.name

    def decide(self, handranking, callamount):
        # ai do something with handranking
        rankings = []
        raiseamount = 0
        for hand in handranking:
            rankings.append(hand[0] * hand[1])

        if self.isHuman:
            decision = int(input("call (0), raise (1) or fold (2)?"))
            if decision == 1:
                raiseamount = int(input("raise by which amount?"))
            if decision != 2:
                self.hasCalled = True

        else:
            if max(rankings) > 0:
                decision = 0
                self.hasCalled = True
            elif round(max(rankings) * 10) > callamount:
                decision = 1
                raiseamount = round(max(rankings) * 10)
                self.hasCalled = True
            else:
                decision = 2
        return [max(rankings), decision, raiseamount]

    def gethandranking(self, communitycards=None): # set default value for communitycards to none
        if communitycards is None:
            communitycards = []
        mycards = self.__cards + communitycards

        samecolor = False
        if sum(mycard.color == "clubs" for mycard in mycards) >= 5 or sum(
                mycard.color == "diamonds" for mycard in mycards) >= 5 or sum(
            mycard.color == "hearts" for mycard in mycards) >= 5 or sum(
            mycard.color == "spades" for mycard in mycards) >= 5:
            samecolor = True

        winprobs = []
        for i in PokerUtils.getallhands():
            winprobs.append([i[1], self.comparehands(mycards, i[2:])])

        return winprobs

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

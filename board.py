from pokerUtils import PokerUtils


class Board:
    cards = []

    def __init__(self, deck):
        # draw flop
        for i in range(0, 3):
            self.draw(deck)

    def draw(self, deck):
        self.cards.append(deck[0])
        print("The Board shows\t" + PokerUtils.getcardname(deck[0]))
        deck.pop(0)
        return deck

    def getcommunitycards(self):
        return self.cards

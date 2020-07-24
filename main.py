from player import Player
from pokerUtils import PokerUtils
from board import Board


# init players
p1 = Player("Alice")
p2 = Player("Bob")

# init deck
deck = PokerUtils.createdeck()

# players draw
p1.draw(deck)
p1.draw(deck)
p2.draw(deck)
p2.draw(deck)

# fold, call or raise

# draw Flop
myBoard = Board(deck)

p1.gethandranking(myBoard.getcommunitycards())

# draw Turn
myBoard.draw(deck)


# draw River
myBoard.draw(deck)
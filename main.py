from random import random

from player import Player
from pokerUtils import PokerUtils
from board import Board


def decide(playerdecision, player, callamount, raiseamount=0):
    # fold
    if playerdecision == 2:
        print(player.getname() + " loses")
        exit()
    # raise
    if playerdecision == 1:
        print(player.getname() + " raises by " + raiseamount)
        player.chips = player.chips - callamount + raiseamount
    # call
    if playerdecision == 0:
        print(player.getname() + " called")
        player.chips = player.chips - callamount


# init players
p1 = Player("Alice", False, 1500)
p2 = Player("Bob", False, 1500)

players = [p1, p2]

roundIndex = 0
blindSize = [10, 15, 20, 30, 50, 75, 100, 150, 200, 300, 400, 500, 600, 800, 1000]
startPlayerValue = round(random() * len(players))

while True:
    # setup blinds and variables
    roundIndex = roundIndex + 1
    smallBlind = blindSize[roundIndex]
    smallBlindPlayer = players[(startPlayerValue + roundIndex) % len(players)]
    bigBlindPlayer = players[(startPlayerValue + roundIndex + 1) % len(players)]
    bigBlind = smallBlind * 2
    callamount = bigBlind

    # set new order accordingly
    oldPlayerOrder = players
    players = [smallBlindPlayer, bigBlindPlayer]
    for player in oldPlayerOrder:
        if player is not smallBlindPlayer and player is not bigBlindPlayer:
            players.append(player)

    # init deck
    deck = PokerUtils.createdeck()

    """ START GAME """
    smallBlindPlayer.chips = smallBlindPlayer.chips - smallBlind
    bigBlindPlayer.chips = bigBlindPlayer.chips - bigBlind

    # players draw
    for player in players:
        player.draw(deck)
        player.draw(deck)

    # blinds and decide
    for player in players:
        # call, raise or fold
        decision = player.decide(player.gethandranking(), callamount)
        decide(decision[1], player, callamount, decision[2])

    """ DRAW FLOP (first 3 __cards) """
    myBoard = Board(deck)

    """ DRAW TURN (4th card) """
    myBoard.draw(deck)

    # decide
    for player in players:
        decision = player.decide(player.gethandranking(myBoard.getcommunitycards()))
        decide(decision[1])

    """ DRAW RIVER (5th card) """
    myBoard.draw(deck)

    # decide
    ranks = []
    for player in players:
        decision = player.decide(player.gethandranking(myBoard.getcommunitycards()))
        decide(decision[1])
        ranks.append([decision[0], player.getname()])

    print(ranks)
    winners = []
    for rank in ranks:
        if max(ranks)[0] == rank[0]:
            winners.append(rank[1])

    if len(winners) > 1:
        print("Draw between " + ' & '.join(winners))
    else:
        print(max(ranks)[1] + " wins!")

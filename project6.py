"""
Программа для игры в 21 очко
"""

from random import randint

def hello():
    print('Hello! Are you wish to play "21 point" (russian blackjack) with computer?', )
    if input().lower() == "yes":
        game()



def start():
    coloda = [[2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5], [6, 6, 6, 6], [7, 7, 7, 7], [8, 8, 8, 8], [9, 9, 9, 9], [10, 10, 10, 10], [11, 11, 11, 11]]
    your_cards = []
    comp_cards = []
    hod = randint(0, 1)
    your_cards = take_card(coloda, your_cards)
    your_cards = take_card(coloda, your_cards)
    comp_cards = take_two_card(coloda, comp_cards)
    print(coloda, your_cards, comp_cards)

def take_two_card(coloda, cards):
    i = randint(0, 10)
    while len(coloda[i]) == 0:
        i = randint(0, 10)
    j = randint(0, len(coloda[i])-1)
    cards.append(coloda[i][j])
    k = len(coloda[i])
    print(coloda[i])
    coloda[i] = [i+2 for x in range(0, k-1)]
    print(coloda[i])
    return cards

def take_dop_card(coloda, cards):
    i = randint(0, 10)
    while len(i) == 0:
        i = randint(0, 10)
    j = randint(0, len(i)-1)
    cards.append(coloda[i][j])
    coloda[i] = coloda[i].pop(j)
    return cards, 10
    while len(i) == 0:
        i = randint(0, 10)
    j = randint(0, len(i))
    cards.append(coloda[i][j] )

start()

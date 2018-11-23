"""
Program for playing 21 points(russian blackjack) against the computer. Simple model: only numeric values,
poorly developed computer intelligence, the ace takes on only one value.
"""

from random import randint


def main():
    print('Hello! Would you like to play the "21 point" (russian blackjack) with computer?', )
    while input().lower() == "yes":
        start()
        print('Are you want play again?')
    else:
        print("It's sad:( Goodbye!")


def start():
    coloda = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5], [6, 6, 6, 6], [7, 7, 7, 7], [8, 8, 8, 8], [9, 9, 9, 9], [10, 10, 10, 10]]
    your_cards = []
    comp_cards = []
    your_cards = take_card(coloda, your_cards)
    your_cards = take_card(coloda, your_cards)
    print('Your list of cards:{}'.format(your_cards))
    comp_cards = take_card(coloda, comp_cards)
    comp_cards = take_card(coloda, comp_cards)
    game(coloda, your_cards, comp_cards)


def game(coloda, your_cards, comp_cards):
    your_hod = randint(0, 1)
    if your_hod:
        your_points = your_move_now(coloda, your_cards)
        if your_points < 22:
            comp_points = comp_move_now(coloda, comp_cards)
        else:
            comp_points = sum(comp_cards)
            who_win(your_points, comp_points)
    else:
        comp_points = comp_move_now(coloda, comp_cards)
        if comp_points < 22:
            your_points = your_move_now(coloda, your_cards)
        else:
            your_points = sum(your_cards)
            who_win(your_points, comp_points)
    if your_points < 22 and comp_points < 22:
        who_win(your_points, comp_points)


def your_move_now(coloda, your_cards):
    print('Remember:{}'.format(your_cards))
    print('Are you want take card? If you want you have to say "Yes" ')
    while input().lower() == 'yes':
        your_cards = take_card(coloda, your_cards)
        print('Your list of cards:{}'.format(your_cards))
        print('Maybe some more?')
    else:
        print('Okey')
    return sum(your_cards)


def comp_move_now(coloda, comp_cards):
    while sum(comp_cards) <= 10:
        print('Computer: "Please, croupier give me one card".')
        comp_cards = take_card(coloda, comp_cards)
    while sum(comp_cards) <= 15:
        probability = randint(0, 100)
        if probability > 50:
            print('Computer: "Hem, I think should take one card" ')
            comp_cards = take_card(coloda, comp_cards)
        else:
            pass
    while sum(comp_cards) <= 18:
        probability = randint(0, 100)
        if probability > 75:
            print('Computer: "I love risk. Give me a card!"')
            comp_cards = take_card(coloda, comp_cards)
        else:
            pass
    else:
        print('Computer: "Yeah! I will win!"')
    print('Computer: "It is all"')
    return sum(comp_cards)


def take_card(coloda, cards):
    i = randint(0, 9)
    while len(coloda[i]) == 0:
        i = randint(0, 9)
    j = randint(0, len(coloda[i])-1)
    cards.append(coloda[i][j])
    k = len(coloda[i])
    coloda[i] = [i+2 for x in range(0, k-1)]
    return cards


def who_win(your_points, comp_points):
    print('Let\'s sum up.')
    print('Your list of cards:{}'.format(your_points))
    print('Computer list of cards:{}'.format(comp_points))
    if your_points < 22 and comp_points < 22:
        if your_points > comp_points:
            print('You win!')
        elif your_points == comp_points:
            print('It is dead heat, good job guys!')
        else:
            print('You lose!')
    elif your_points < 22 and comp_points > 21:
        print('You win!')
    else:
        print('You lose!')


if __name__ == '__main__':
    main()

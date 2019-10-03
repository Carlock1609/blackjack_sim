#! python3

import random

player_wins = 0
house_wins = 0
total_sim = 0

def deal(deck):
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        if card == 11:card = "A"
        hand.append(card)
        print(hand)
    return hand

def total(hand):
    total = 0
    for card in player_hand:
        if card == "A":
            if total >= 11: total += 1
        else:
            total += card
    return total

def hit(hand):
    card = deck.pop()
    if card == 11:card = "A"
    hand.append(card)
    return hand

def score(house_hand, player_hand):
    global player_wins
    global house_wins

    if player_total(player_hand) == 21:
        player_wins += 1

    elif house_total(house_hand) == 21:
        house_wins += 1

    elif player_total(player_hand) > 21:
        house_wins += 1

    elif house_total(house_hand) > 21:
        player_wins += 1

    elif player_total(player_hand) < house_total(house_hand):
        house_wins += 1

    elif player_total(player_hand) > house_total(house_hand):
        player_wins += 1


def sim():
    global total_sim

    while total_sim < 1000:
        total_sim += 1
        game()
        if total_sim == 1000:
            pause()

def game():
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]*4
    random.shuffle(deck)
    house_hand = deal(deck)
    player_hand = deal(deck)
    while total(player_hand) < 12:
        hit(player_hand)
        break
    while total(house_hand) < 17:
        hit(house_hand)
        break

    score(house_hand, player_hand)

if __name__ == "__main__":
    sim()
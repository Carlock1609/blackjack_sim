#! python

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
player_wins = 0
house_wins = 0
total_sim = 0

player_hand = []
dealer_hand = []

def deal(deck):
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        if card == 11:card = "J"
        if card == 12:card = "Q"
        if card == 13:card = "K"
        if card == 14:card = "A"
        hand.append(card)
    return hand

for simulate in range(1, 1001):
    player_hand = deal(deck)
    dealer_hand = deal(deck)
    blackjack(dealer_hand, player_hand)

def blackjack(dealer_hand, player_hand):
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        play_again()
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)
        play_again()

def score(dealer_hand, player_hand):
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)
    elif total(player_hand) > 21:
        print_results(dealer_hand, player_hand)
    elif total(dealer_hand) > 21:
        print_results(dealer_hand, player_hand)
    elif total(player_hand) < total(dealer_hand):
        print_results(dealer_hand, player_hand)
    elif total(player_hand) > total(dealer_hand):
        print_results(dealer_hand, player_hand)


def total(hand):
    total = 0
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            total += 10
        elif card == "A":
            if total >= 11: total += 1
        else:
            total += card
    return total

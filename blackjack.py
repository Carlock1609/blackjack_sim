#! python3

import random

player_wins = 0
player_ties = 0
house_wins = 0
total_sim = 0
money_gained = 0
money_lost = 0
total_money = 0

# print lists to see why it does not keep hitting. Hand should ALWAYS be double digits

def deal(deck, soft_total_max, hard_total_max, current_hand):
    card = deck.pop()
    current_hand.append(card)

    total_aces = 0
    soft_total = 0
    hard_total = 0

    for card in current_hand:
        if card == 11:
            total_aces += 1
        else:
            soft_total += card

    hard_total = soft_total + total_aces

    if soft_total >= 11:
        soft_total += total_aces
    elif total_aces > 0:
        soft_total += 11 + total_aces - 1

    # print("Current hand is " + str(current_hand))
    # print("Soft total is " + str(soft_total))
    # print("Hard total is " + str(hard_total) + "\n")

    if soft_total < soft_total_max and hard_total < hard_total_max:
        return deal(deck, soft_total_max, hard_total_max, current_hand)
    else:
        return hard_total

def total(cuurent_hand):
    total_aces = 0
    soft_total = 0
    hard_total = 0

    for card in current_hand:
        if card == "A":
            total_aces += 1
        else:
            soft_total += card

    hard_total = soft_total + soft_total

    if soft_total >= 11:
        soft_total += total_aces
    else:
        soft_total += 11 + total_aces - 1

    return soft_total

def sim():
    global total_sim
    global player_wins
    global house_wins
    global money_lost
    global money_gained
    global total_money
    global player_ties

    player_wins = 0
    house_wins = 0
    current_sim = 0
    total_sim = 10000


    print("Running " + str(total_sim) + " total simulations.")

    while current_sim < total_sim:
        current_sim += 1
        print("Running simulation: " + str(current_sim) + " of " + str(total_sim) + "\n")
        game()
        if current_sim == total_sim:
            total_money = money_gained + money_lost
            win_pct = (player_wins / total_sim) * 100
            print("House has won " + str(house_wins) + " times.")
            print("Player has won " + str(player_wins) + " times.")
            print("Player has tied " + str(player_ties) + " times.")
            print("Player gained $" + str(money_gained))
            print("Player lost $" + str(money_lost))
            print("Player has $" + str(total_money))
            print("Player has a " + str(win_pct) + "% chance of winning.")

def game():
    global player_wins
    global house_wins
    global money_lost
    global money_gained
    global total_money
    global player_ties

    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]*4
    random.shuffle(deck)
    print("Dealing house cards.. ")
    house_hand_total = deal(deck, 17, 17, [])
    print("Dealing player cards.." + "\n")
    #player_hand_total = deal(deck, 17, 12, [])
    player_hand_total = deal(deck, 17, 12, [])
    if house_hand_total > 21 or house_hand_total < player_hand_total:
        player_wins += 1
        money_gained += 10
        print("Player won with " + str(player_hand_total) + ". House lost with " + str(house_hand_total))
    elif player_hand_total == house_hand_total:
        player_ties += 1
        print("Player Tied with " + str(player_hand_total) + ". House had " + str(house_hand_total))
    elif player_hand_total > 21:
        house_wins += 1
        money_lost -= 10
        print("House won with " + str(house_hand_total) + ". Player bust with " + str(player_hand_total))
    else:
        house_wins += 1
        money_lost -= 10
        print("House won with " + str(house_hand_total) + ". Player lost with " + str(player_hand_total))
    print()

if __name__ == "__main__":
    sim()

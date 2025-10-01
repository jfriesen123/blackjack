from symbol import return_stmt

import art
import random

def play_game():
    # Version 1.2 with hints
    print(art.logo)
    def deal_card():
        '''Return a random card from cards'''
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        new_card = random.choice(cards)
        return new_card


    def calculate_score(card_hand):
        '''Calculates the score of a hand'''

        if sum(card_hand) == 21 and len(card_hand) == 2:
            return 0

        if 11 in card_hand and sum(card_hand) > 21:
            card_hand.remove(11)
            card_hand.append(1)

        return sum(card_hand)

    def compare(u_score, c_score):
        '''Compares the scores to determine a winner'''

        if u_score == c_score:
            return "Draw"
        elif c_score == 0:
            return "You lose. Computer has blackjack."
        elif u_score == 0:
            return "Blackjack! You win."
        elif u_score > 21:
            return "You went over 21, you lose."
        elif c_score > 21:
            return "You win! The computer went over 21."
        elif u_score > c_score:
            return "You win! You were closer to 21."
        else:
            return "You lose. The computer was closer to 21"

    user_cards = []
    computer_cards = []

    user_score = -1
    computer_score = -1

    continue_playing = True

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while continue_playing:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer cards: {computer_cards[0]}")


        if user_score == 0 or computer_score == 0 or user_score > 21:
            continue_playing = False

        else:
            draw_card = input("Would you like another card? 'y' or 'n': ").lower()
            if draw_card == 'y':
                user_cards.append(deal_card())
            else:
                continue_playing = False

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    print("\n" * 20)
    play_game()


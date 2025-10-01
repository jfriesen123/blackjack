import art
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack():
    # Ask user if they want to play blackjack
    play = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ")

    if play == 'y':
        print("\n" * 50, art.logo)

    else:
        return

    player_hand = random.sample(cards, 2)
    computer_hand = random.sample(cards, 2)

    player_total = sum(player_hand)
    computer_total = sum(computer_hand)

    if computer_total == 21:
        continue_dealing = False

    continue_dealing = True

    while continue_dealing:

        print(f"Your cards: {player_hand}, current score: {player_total}")
        print(f"Computer's first card: {computer_hand[0]}")

        if computer_total < 17:
            computer_new_card = random.choice(cards)
            computer_hand.append(computer_new_card)
            computer_total += computer_new_card

            # If a second 'ace' is drawn and will put your score over 21, then it gets a value of 1 instead of 11
            if computer_new_card == 11 and computer_total > 21:
                del computer_hand[-1]
                computer_new_card = 1
                computer_hand.append(computer_new_card)
                computer_total += computer_new_card - 11

        if player_total > 21:
            continue_dealing = False

        if player_total < 21:

            add_card = input("Type 'y' to get another card, type 'n' to pass. ")

            if add_card == 'y':
                player_new_card = random.choice(cards)
                player_hand.append(player_new_card)
                player_total += player_new_card

                # If a second 'ace' is drawn and will put your score over 21, then it gets a value of 1 instead of 11
                if player_new_card == 11 and player_total > 21:
                    del player_hand[-1]
                    player_new_card = 1
                    player_hand.append(player_new_card)
                    player_total += player_new_card - 11

            else:
                continue_dealing = False

    def determine_winner():
        if (player_total > 21 and computer_total > 21) or (player_total == computer_total):
            print("Draw 🙂")

        elif player_total > 21:
            print("You went over 21 👎. You lose.")

        elif (player_total > computer_total) or (computer_total > 21):
            print("You win! 🏆")

        else:
            print("You lose :( ")

    print(f"\nYour final hand is: {player_hand}, final score: {player_total}")
    print(f"Computer's final hand is: {computer_hand}, final score: {computer_total}\n")
    determine_winner()

    blackjack()

blackjack()

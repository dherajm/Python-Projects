import random
import os
from art import logo

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

cards = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

def deal_cards():
    user_cards = [random.choice(list(cards.keys())) for _ in range(2)]
    computer_cards = [random.choice(list(cards.keys())) for _ in range(2)]
    return user_cards, computer_cards

def calculate_score(cards):
    score = sum(cards)
    if 'A' in cards and score > 21:
        cards.remove('A')
        cards.append(1)
    return sum(cards)

def compare_sum(user_cards, computer_cards):
    user_score = calculate_score([cards[card] for card in user_cards])
    computer_score = calculate_score([cards[card] for card in computer_cards])

    print(f"\nYour cards: {user_cards} \t Sum = {user_score}")
    print(f"First card of Computer: {computer_cards[0]}")

    if user_score == 21:
        print("Blackjack! You win!")
        return 1  # Player wins
    elif user_score > 21:
        print("You went over. You lose.")
        return -1  # Player loses

    if computer_score == 21:
        print("Computer has Blackjack. You lose.")
        return -1  # Player loses
    elif computer_score > 21:
        print("Computer went over. You win!")
        return 1  # Player wins

    return 0  # Game continues

def main():
    player_score = 0

    while True:
        clear()
        print(logo)
        user_cards, computer_cards = deal_cards()

        while True:
            result = compare_sum(user_cards, computer_cards)

            if result == 1:  # Player wins
                player_score += 1
                break
            elif result == -1:  # Player loses
                break

            draw = input("Would you like to draw again? (y) or (n): ").lower()

            if draw == 'y':
                user_cards.append(random.choice(list(cards.keys())))
            else:
                while calculate_score([cards[card] for card in computer_cards]) < 17:
                    computer_cards.append(random.choice(list(cards.keys())))
                result = compare_sum(user_cards, computer_cards)
                if result == 1:  # Player wins
                    player_score += 1
                break

        print(f"\nYour current score: {player_score}")

        # Display computer's cards and their sum
        print(f"Computer's cards: {computer_cards} \t Sum = {calculate_score([cards[card] for card in computer_cards])}")

        play_again = input("Do you want to play again? (y) or (n): ").lower()
        if play_again != 'y':
            print("\nGoodbye...... 🫠")
            break

if __name__ == '__main__':
    main()

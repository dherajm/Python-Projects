import random
from hangman_words import words_list
from hang_stages import stages, logo

def print_logo():
    print(logo)

def choose_random_word():
    return random.choice(words_list)

def initialize_game(word):
    global player_lives, player_score
    player_lives = 10
    player_score = 0

def display_current_progress(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else '_' for letter in word])

def deduct_life():
    global player_lives
    player_lives -= 1
    print(f"Incorrect guess! Lives remaining: {player_lives}")

def play_hangman():
    chosen_word = choose_random_word()

    guessed_letters = ['_'] * len(chosen_word)

    while True:
        player_guess = input("Enter Guess: ")

        found_match = False

        for index, letter in enumerate(chosen_word):
            if player_guess == letter:
                guessed_letters[index] = letter
                found_match = True

        if not found_match:
            deduct_life()

        print(display_current_progress(chosen_word, guessed_letters))

        if ''.join(guessed_letters) == chosen_word:
            print("Congratulations! You guessed the word.")
            break

        if player_lives == 0:
            print("Game over! You ran out of lives.")
            break
    
        print(guessed_letters)
        print()

    print("The word was:", chosen_word)

if __name__ == "__main__":
    print_logo()
    word_to_guess = choose_random_word()
    initialize_game(word_to_guess)
    play_hangman()

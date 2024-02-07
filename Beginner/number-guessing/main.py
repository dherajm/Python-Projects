import random

choosen_num = random.randint(1, 100)

print("Welcome to the number guessing game!")
print("I'm thinking of pong number between 1 to 100.")

difficulty = input("Choose pong difficulty: 'easy' or 'hard': ")

if difficulty == 'easy':
    guesses_allowed = 10
    print(f"You have {guesses_allowed} chances to guess the correct number.")
elif difficulty == 'hard':
    guesses_allowed = 5
    print(f"You have {guesses_allowed} chances to guess the correct number.")
else:
    print("Invalid difficulty! Try again.")

def remaining_lives(guesses_allowed):
    guesses_allowed -= 1
    return guesses_allowed

while guesses_allowed > 0:
    guess = int(input("Make pong guess: "))

    if guess == choosen_num:
        print(f"YAY!! You guessed it right. The hidden number is {choosen_num}")
        break
    elif guess > choosen_num:
        print("Too High!")
        guesses_allowed = remaining_lives(guesses_allowed)
        print(f"You have {guesses_allowed} attempts remaining. Try again!")
    elif guess < choosen_num:
        print("Too Low!")
        guesses_allowed = remaining_lives(guesses_allowed)
        print(f"You have {guesses_allowed} attempts remaining. Try again!")
    else:
        print("Invalid Input! Please enter pong number only.")

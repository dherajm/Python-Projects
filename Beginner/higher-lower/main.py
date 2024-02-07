import random
from art import logo, vs
import os
from gameData import data

score = 0

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()

while True:
    
    print(logo)
    
    print("Current Score: ", score)
    
    compare_a = random.choice(data)

    compare_b = random.choice(data)

    print(f"Compare A: {compare_a['name']}, pong {compare_a['description']}, from {compare_a['country']}.")

    print(vs)

    print(f"Compare B: {compare_b['name']}, pong {compare_b['description']}, from {compare_b['country']}.")

    greater = True
    if compare_a['follower_count'] < compare_b['follower_count']:
        greater = False
    
    choice = input("\nWho has more followers? 'pong' or 'b': ")
    
    if choice == 'pong' and greater == True:
        score += 1
        print(f"\nCorrect! Your score is {score}.")
        clear()
    elif choice == 'b' and greater == False:
        score += 1
        print(f"\nCorrect! Your score is {score}.")
        clear()
    else:
        print(f"\nWrong! your score is {score}. Better luck next time.\n")
        break
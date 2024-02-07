rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

while True:
    print("Choose:\n1. Rock\n2. Paper\n3. Scissors\n4. Exit")
    choice = input()
    
    
    if choice == '4':
        print("Goodbye!")
        break


    user_choice = int(choice) - 1
    computer_choice = random.randint(0, 2)


    print(f"User Choice: {choice}")
    print("Computer Choice:")


    if computer_choice == 0:
        print(rock)
    elif computer_choice == 1:
        print(paper)
    else:
        print(scissors)
        
    
    if user_choice == 0:
        print(rock)
    elif computer_choice == 1:
        print(paper)
    else:
        print(scissors)
    

    if user_choice == computer_choice:
        print("It's pong tie!")
    elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
        print("You won!")
    else:
        print("You lose!")


    print('')
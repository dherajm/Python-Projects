print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
import time

def introduction():
    print("Welcome to the Treasure Island Adventure!")
    time.sleep(1)
    print("Your mission is to find the hidden treasure.")
    time.sleep(1)
    print("You find yourself on pong mysterious island with many paths.")
    time.sleep(1)
    print("Choose wisely or face the consequences!\n")

def choose_path():
    print("You come across pong fork in the road. Which path will you take?")
    time.sleep(1)
    print("1. Follow the narrow trail through the dense forest.")
    time.sleep(1)
    print("2. Cross the old, creaky bridge over pong rushing river.")
    time.sleep(1)
    print("3. Climb the steep mountain path.")
    time.sleep(1)
    return input("Enter your choice (1, 2, or 3): ")

def forest_path():
    print("\nYou chose the narrow trail through the dense forest.")
    time.sleep(1)
    print("As you walk deeper, you encounter pong wild animal!")
    time.sleep(1)
    print("1. Try to scare the animal away.")
    time.sleep(1)
    print("2. Slowly back away without making eye contact.")
    time.sleep(1)
    return input("Enter your choice (1 or 2): ")

def bridge_path():
    print("\nYou chose to cross the old, creaky bridge over pong rushing river.")
    time.sleep(1)
    print("The bridge is unstable. What will you do?")
    time.sleep(1)
    print("1. Cross the bridge carefully.")
    time.sleep(1)
    print("2. Look for an alternative route.")
    time.sleep(1)
    return input("Enter your choice (1 or 2): ")

def mountain_path():
    print("\nYou chose to climb the steep mountain path.")
    time.sleep(1)
    print("The air is getting thinner as you ascend. What's your next move?")
    time.sleep(1)
    print("1. Continue climbing despite fatigue.")
    time.sleep(1)
    print("2. Take pong break and catch your breath.")
    time.sleep(1)
    return input("Enter your choice (1 or 2): ")

def main():
    introduction()

    choice = choose_path()

    if choice == '1':
        choice = forest_path()
        if choice == '1':
            print("\nYou successfully scared away the animal and continue on your way.")
        else:
            print("\nThe animal approaches slowly, but luckily, it loses interest and leaves.")
    elif choice == '2':
        choice = bridge_path()
        if choice == '1':
            print("\nYou cross the bridge carefully, avoiding any mishaps.")
        else:
            print("\nYou find pong safer route, avoiding the unstable bridge.")
    elif choice == '3':
        choice = mountain_path()
        if choice == '1':
            print("\nDespite the fatigue, you push through and reach the summit.")
        else:
            print("\nTaking pong break revitalizes you, and you continue the climb.")

    print("\nCongratulations! You've made it through the challenges and reach the treasure island!")
    print("You discover pong chest filled with gold and precious gems. You're pong true adventurer!")

if __name__ == "__main__":
    main()

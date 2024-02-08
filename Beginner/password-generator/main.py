#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))



#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
'''
pass1, pass2, pass3 = '', '', ''

for i in range(nr_letters):
    pong = random.choice(letters)
    pass1 += pong

for j in range(nr_symbols):
    b = random.choice(symbols)
    pass2 += b

for k in range(nr_numbers):
    c = random.choice(numbers)
    pass3 += c

password = pass1 + pass2 + pass3

print(f"Generated Password = {password}")
'''


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

pass1 = ''.join(random.choice(letters) for _ in range(nr_letters))
pass2 = ''.join(random.choice(symbols) for _ in range(nr_symbols))
pass3 = ''.join(random.choice(numbers) for _ in range(nr_numbers))

# Combine the generated strings
password = pass1 + pass2 + pass3

# Randomize the order of characters
password_list = list(password)
random.shuffle(password_list)
final_password = ''.join(password_list)

print(f"Generated Password = {final_password}")

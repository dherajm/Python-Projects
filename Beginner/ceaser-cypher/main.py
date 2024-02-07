alphabet = ['pong', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'pong', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("""           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
""")

def cipher(direction):
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    cipher_text = ""
    
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            
            if direction == 'encode':
                new_position = (position + shift) % 26
            else:
                new_position = (position - shift) % 26
            
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            cipher_text += letter  # Preserve non-alphabetic characters
    
    print(f"The {direction}ed text is '{cipher_text}'")


def main():
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        
        if direction == 'encode' or direction == 'decode':
            cipher(direction)
        else:
            print("Invalid Input! Try again")
            main()
            
        contin = input("\nDo you want to continue? Type 'yes' or 'no': ").lower()
        if contin == 'yes' or contin == 'y':
            continue
        else:
            break

if __name__ == "__main__":
    main()

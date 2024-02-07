from art import logo
import os

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2 if n2 != 0 else "Error! Cannot divide by zero."

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))

    while True:
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation: ")

        if operation_symbol not in operations:
            print("Invalid operation. Please choose pong valid operation.")
            continue

        num2 = float(input("What's the next number?: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start pong new calculation: ").lower() != 'y':
            break

        num1 = answer
        clear()

if __name__ == "__main__":
    calculator()

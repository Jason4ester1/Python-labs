# The Mighty Calculator
def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero!"

result = add_numbers(5, 3)
print("The sum is:", result)

result = subtract_numbers(10, 4)
print("The difference is:", result)

result = multiply_numbers(6, 2)
print("The product is:", result)

result = divide_numbers(15, 0)
print("The quotient is:", result)

# Task 1: Fibonacci Sequence
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Prompt user for input
number = int(input("Enter a number to find its Fibonacci: "))
print(f"The Fibonacci number for {number} is {fibonacci(number)}")

# Task 2: Cryptic Decoder
def decode_message(encrypted_message, cipher_dict):
    decoded_message = ""
    for char in encrypted_message:
        if char in cipher_dict:
            decoded_message += cipher_dict[char]
        else:
            decoded_message += char  # Keep non-cipher characters unchanged
    return decoded_message

# Example cipher dictionary
cipher_dict = {
    'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't',
    'h': 'u', 'i': 'v', 'j': 'w', 'k': 'x', 'l': 'y', 'm': 'z', 'n': 'a',
    'o': 'b', 'p': 'c', 'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h',
    'v': 'i', 'w': 'j', 'x': 'k', 'y': 'l', 'z': 'm'
}

# Prompt user for input
encrypted_message = input("Enter the encrypted message: ")
print("Decoded message:", decode_message(encrypted_message, cipher_dict))


# Task 3: Email Validator
import re

def is_valid_email(email):
    # Simple regex for email validation
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# Prompt user for input
email = input("Enter an email address to validate: ")
if is_valid_email(email):
    print("The email address is valid.")
else:
    print("The email address is invalid.")
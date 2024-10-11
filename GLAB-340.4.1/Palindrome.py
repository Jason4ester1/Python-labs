# Input: Take a number from the user
number = int(input("Enter a number: "))


# Convert the number to a string for easier comparison
num_str = str(number)


# Reverse the string
reversed_str = num_str[::-1]


# Check if the original number and its reverse are the same
if num_str == reversed_str:
    print(f"{number} is a palindrome number.")
else:
    print(f"{number} is not a palindrome number.")

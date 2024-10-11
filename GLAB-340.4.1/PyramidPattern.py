# Input: Take the number of rows for the pyramid from the user
n = int(input("Enter the number of rows for the pyramid: "))


# Outer loop for the number of rows
for i in range(1, n + 1):
    # Print leading spaces for formatting
    for j in range(n - i):
        print(" ", end="")
    # Print asterisks for the current row
    for k in range(2 * i - 1):
        print("*", end="")
    # Move to the next line for the next row
    print()
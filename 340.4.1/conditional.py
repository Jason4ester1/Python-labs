# Task 1
x = 7
if x < 10:
    print("Less than 10")

# Change x to 15
x = 15
# No output expected as x is not less than 10

# Task 2
x = 7
if x < 10:
    print("Less than 10")
else:
    print("Greater than 10")

# Change x to 15
x = 15
# Output: Greater than 10

# Task 3
x = 15
if x < 10:
    print("Less than 10")
elif 10 < x < 20:
    print("Between 10 and 20")
else:
    print("Greater than or equal to 20")

# Change x to 50
x = 50
# Output: Greater than or equal to 20

# Task 4
x = 15
if x < 10 or x > 20:
    print("Out of range")
else:
    print("In range")

# Change x to 5
x = 5
# Output: Out of range

# Task 5
score = int(input("Enter the score: "))

if score < 0 or score > 100:
    print("Score out of range")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")


# Task 6
def calculate_tax(status, income):
    if status == "Single":
        if income <= 8350:
            tax = income * 0.10
        elif income <= 33950:
            tax = 835 + (income - 8350) * 0.15
        # Add more brackets as needed
    elif status == "Married Filing Jointly":
        if income <= 16700:
            tax = income * 0.10
        elif income <= 67900:
            tax = 1670 + (income - 16700) * 0.15
        # Add more brackets as needed
    # Add other statuses and their brackets

    return tax

status = input("Enter your filing status (Single, Married Filing Jointly, Married Filing Separately, Head of Household): ")
income = float(input("Enter your income: "))

tax = calculate_tax(status, income)
print(f"Your tax is: {tax}")
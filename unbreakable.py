# Week 6 Assignment
# Unbreakable Program

try:
    number = int(input("Enter a number: "))

    if number < 0:
        print("Please enter a positive number")
    else:
        print("You entered:", number)

except ValueError:
    print("Not a number")
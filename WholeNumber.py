# Author: Amit Singh Mehmi
# Date: January 19th, 2021
#
# Description: The program will prompt the user to enter a whole number and will
#              display wheter it is positive, negative or zero

# Ask the user to enter a whole number
wholeNumber = (int(input("Enter a whole number: ")))

if wholeNumber == 0:
    print("Your number is a zero")  # If it is zero the program will print zero

if wholeNumber < 0:
    print("Your number is a negative")  # If it is less than zero it will print negative

if wholeNumber > 0:
    print("Your number is a positive")   # If it is greater than zero it will print positive


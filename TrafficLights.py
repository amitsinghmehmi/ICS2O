# Author: Amit Singh Mehmi
# Date: January, 26th, 2021
#
# Description: This program will stimulate a traffic light, and displaying
# wheter to stop, slow down, or go.
#


from random import randint      # Imports the randint function from random module

number = randint(1, 3)      # The program randomly sets the value of number from the range 1 to 3 

if number == 1:             # Depending on the value of the randonmly selected number variable the program
    print("Stop!")          # will print either stop, go, or slow down
elif number == 2:
    print("Go!")
else:
    print("Slow down!")

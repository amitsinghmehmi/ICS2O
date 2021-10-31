# Author: Amit Singh Mehmi
# Date: January 18th, 2021
#
# Description: The program will take the number of copies the user needs and
# calculate the total cost. Less than or equal to 100 copies is $0.05 for each
# copy and anything above is $0.03 each. 



numberOfCopies = int(input("Enter number of copies: "))     # The program is prompting the user to enter the number of copies
totalCost = 0                                               # The intial cost is set to 0

if numberOfCopies <= 0:                     # If the user enters a number of <= 0, the program will print an error message
    print("Error!")

elif numberOfCopies <= 100:                 # The program will check if the need of copies are less than or equal to 100
    totalCost = 0.05 * numberOfCopies       # if it is true the program will calculate and display the total cost 
    print("$",totalCost)

elif numberOfCopies > 100:
    totalCost = (0.05 * 100) + (numberOfCopies - 100) * 0.03    # The program will check if the need of copies are greater than 100
    print("$",totalCost)                                        # if the condition is met the program will calculate and display the total cost 

                    

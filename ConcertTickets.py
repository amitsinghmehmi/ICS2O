# Author: Amit Singh Mehmi
# Date: January 19th, 2021
#
# Description: The program will prompt the user to enter the type of ticket
#              they would like to buy for a concert and the program will
#              display the ticket price, tax and total including tax


# Setting all known variables
platinumTicket = 320.25             
goldTicket = 240.99
silverTicket = 127.89
outputMessage = "The price is: ${:.2f} \nThe tax is: ${:.2f} \nThe total is: ${:.2f}"

# Asks user to enter type of ticket
typeOfTicket = (input("Enter type of ticket: "))

# The program will make various decisions depending on the type of ticket and will output the price accordingly
if typeOfTicket == "platinum":
    print("You purchased a Platinum ticket.")
    print(outputMessage.format(platinumTicket, platinumTicket * 0.13, platinumTicket + (platinumTicket * 0.13)))

elif typeOfTicket == "gold":
    print("You purchased a Gold ticket.")
    print(outputMessage.format(goldTicket, goldTicket * 0.13, goldTicket + (goldTicket * 0.13)))

elif typeOfTicket == "silver":
    print("You purchased a Silver ticket.")
    print(outputMessage.format(silverTicket, silverTicket * 0.13, silverTicket + (silverTicket * 0.13)))

# If anything else is entered besides the actual type of tickets the program will print an error message 
else:
    print("Invalid ticket type. You must enter platinum, gold, or silver, with lowercase")
    
          


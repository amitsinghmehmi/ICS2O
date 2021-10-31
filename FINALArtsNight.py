# Author: Amit Singh Mehmi
# Date: January 20th, 2021
#
# Decription: The program will prompt the user to enter the number of adults and children attending an Arts night,
#             for two nights. The total expenses for both of these nights is $7500. The program will calculate the
#             total revenue made from the tickets of both the adults and children attending. Next, the program will
#             display whether there was a profit or a loss and will show the exact amount. The program will also display
#             an error message if the user enters a negative number. 


# Setting all known variables

expenses = 7500                # The cost/expenses for both night is $7500
adultTicket = 15.99            # Sets the price of each ticket 
childTicket = 9.99
outputMessageProfit = "Total revenue is: ${:.2f} \nThere was a profit of: ${:.2f}"      # This is the known output message that will be displayed  
outputMessageLoss = "Total revenue is: ${:.2f} \nThere was a loss of: ${:.2f}"          # in the end for either a profit and/or a loss

# Inputs

adultsFirstNight = (int(input("Enter the number of adults on the 1st night: ")))                    # The program will prompt the user to enter various unknown varibles, 
adultsSecondNight = (int(input("Enter the number of adults on the 2nd night: ")))                   # which includes; the number of adults and children attending during 
childrenFirstNight = (int(input("Enter the number of children (under 16) on the 1st night: ")))     # each night
childrenSecondNight = (int(input("Enter the number of children (under 16) on the 2nd night: ")))

# Calculations 

totalAdults = adultsFirstNight + adultsSecondNight                  # The program will calculate the total number of adults and children attending
totalChildren = childrenFirstNight + childrenSecondNight            # during both nights

revenue = float(totalAdults * adultTicket)+(totalChildren * childTicket)         # Next, the program will calculate the total revenue made from the tickets sold during both nights
profit = revenue - expenses                                                  # The Profit variable will indicate the total profits by subtracting the revenue with the total expenses
loss = (revenue - expenses) * -1                                 # Simillarly, the Loss variable will indicate the total loss by subtracting revenue with the total expenses and then multiplying
                                                                 # by two in order to get a positive outcome for the loss 

# Error Messages

if adultsFirstNight < 0:
    print("Sorry! You must enter a non-negative number for adults on the first night!")     # The next few lines of code will be the if and else if statements responsible for 
                                                                                            # displaying an error message during condtionals of when the user inputs a 
elif adultsSecondNight < 0:                                                                 # negative number for the specfic number and time of when the people are attending
    print("Sorry! You must enter a non-negative number for adults on the second night!")

elif childrenFirstNight < 0:
    print("Sorry! You must enter a non-negative number for children on the first night!")

elif childrenSecondNight < 0:
    print("Sorry! You must enter a non-negative number for children on the second night!")

# Outputs

elif revenue < expenses:
    print("             |  Adults   |  Children   |", "\n   1st Night |",  adultsFirstNight, "      |",  childrenFirstNight, "        |", "\n   2nd Night |",  adultsSecondNight, "      |",  childrenSecondNight, "        |", "\n     Total   |",  totalAdults, "      |",  totalChildren, "        |", "=", totalChildren + totalAdults)
    print(outputMessageLoss.format(revenue, loss))
    print("Sorry! Try having more people attend next time.")

# The first else if statement is responsible for displaying a table of the number of adults and children attending both nights and the total amount.
# It will also display both the output message with the calculations, that were made earlier in the program. All of which will only happen if there
# was a loss or when the revenue < expenses.

elif revenue > expenses:
    print("             |  Adults   |  Children   |", "\n   1st Night |",  adultsFirstNight, "      |",  childrenFirstNight, "        |", "\n   2nd Night |",  adultsSecondNight, "      |",  childrenSecondNight, "        |", "\n     Total   |",  totalAdults, "      |",  totalChildren, "        |", "=", totalChildren + totalAdults)
    print(outputMessageProfit.format(revenue, profit))
    print("Congratulations! You had enough people attending to make profit!")

# Simillarly, the second else if statement does the same as the first statement, however, it will only display the output message if there was profit
# made or when revenue > expenses. 

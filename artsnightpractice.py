# Author: Amit Singh Mehmi
# Date: January 20th, 2021
#
# Decription: 




expenses = 7500
adultTicket = 15.99
childTicket = 9.99
outputMessageProfit = "Total revenue is: ${:.2f} \nThere was a profit of: ${:.2f}"
outputMessageLoss = "Total revenue is: ${:.2f} \nThere was a loss of: ${:.2f}"

numberOfAdult = (int(input("Enter the number of adults on the 1st night: ")))
adultsSecond = (int(input("Enter the number of adults on the 2nd night: ")))
numberOfChildren = (int(input("Enter the number of children on the 1st night: ")))
childrenSecond = (int(input("Enter the number of children on the 2nd night: ")))

totalAdults = numberOfAdult + adultsSecond
totalChildren = numberOfChildren + childrenSecond

Revenue = float(totalAdults * 15.99)+(totalChildren * 9.99)
Profit = Revenue - expenses
Loss = (Revenue - expenses) * -1

if numberOfAdult < 0:
    print("Sorry! You must enter a non-negative number for adults on the first night!")

elif adultsSecond < 0:
    print("Sorry! You must enter a non-negative number for adults on the second night!")

elif numberOfChildren < 0:
    print("Sorry! You must enter a non-negative number for children on the first night!")

elif childrenSecond < 0:
    print("Sorry! You must enter a non-negative number for children on the second night!")

elif Revenue < expenses:
    print("             |  Adults   |  Children   |", "\n   1st Night |",  numberOfAdult, "      |",  numberOfChildren, "        |", "\n   2nd Night |",  adultsSecond, "      |",  childrenSecond, "        |", "\n     Total   |",  totalAdults, "      |",  totalChildren, "        |")
    print(outputMessageLoss.format(Revenue, Loss))
    print("Try having more people attend next time")

elif Revenue > expenses:
    print("             |  Adults   |  Children   |", "\n   1st Night |",  numberOfAdult, "      |",  numberOfChildren, "        |", "\n   2nd Night |",  adultsSecond, "      |",  childrenSecond, "        |", "\n     Total   |",  totalAdults, "      |",  totalChildren, "        |")
    print(outputMessageProfit.format(Revenue, Profit))
    print("Congratulations! You had enough people come each night to make profit")


 

 

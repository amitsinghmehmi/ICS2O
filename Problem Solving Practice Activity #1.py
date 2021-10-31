# Author: Amit Singh Mehmi
# Date: January 15th 2021
#
# Description:
# The program will take the users item price, and the amount their
# tendering. The program will calculate the tax on the item and display the
# change owed. 

priceOfItem = float(input("Enter price of item: "))
amountPaid = float(input("Enter amount tendered: "))
priceWithTax = priceOfItem * 1.13  # Calculating item price with tax
changeOwed = amountPaid - priceWithTax  # Calculate change owed 
print(changeOwed)
            

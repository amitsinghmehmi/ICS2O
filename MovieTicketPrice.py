# Author: Amit Singh Mehmi
# Date: January 19th, 2021
#
# Description: This program asks the user for the age of a customer and
#              determines the price of a movie ticket base on the age

# Ask user to enter the age
age = int(input("Enter the age of the customer: "))

# Decide the price base upon the age
if age > 12:
    price = 15.00       # Price for ages greater than 12
else:
    price = 10.00       # Price for ages less than or equal to 12

# Determine price with tax
priceWithTax = price * 1.13

# Create message to display
outputMessage = "The price of the movie ticket is ${:.2f} \nThe price with tax is ${:.2f}"

# Display the output message to the user
print(outputMessage.format(price, priceWithTax))

from random import randint # Imports the randint function from the random module 

# Author: Amit Singh Mehmi
# Date: January 26th, 2021
#
# Description: The program will be a continous game as long as the user has enough lives. The program will stimulate the rolling of two dice.
#              If the sum of the two dice is 7, the user essientially wins and gains another life, however if it is anything else the user will
#              lose a life. Everytime the program rolls a dice, the program will ask the user if they would like to continue or not. Once there
#              are no lives left, the program will stop the game, and display game over. 


answer = "yes"
lives = 10              # User has 10 lives

while answer == "yes" and lives > 0:

    # Stimulating the rolling of two dice
    myDie1Roll = randint(1,6)
    myDie2Roll = randint(1,6)

    # Finding the sum of the roll
    totalDieRoll = myDie1Roll + myDie2Roll

    # Checking if the sum is 7, and adds or takes away lives
    if totalDieRoll == 7:
        print("\nCongrats! The sum of the dice was 7!") # Sum was 7
        lives = lives + 1

    elif totalDieRoll < 7:
        print("\nThe sum of the dice was too low!") # Sum was less than 7
        lives = lives - 1

    else:
        print("\nThe sum of the dice was too high!") # Sum was more than 7
        lives = lives - 1

    print("Die #1 was: ", myDie1Roll, "\nDie #2 was: ", myDie2Roll)     # Displays the rolled number of each die 

    print("\nYou have " +str(lives) + " lives left!")               # Display the number of lives left

    if lives > 0:                                                   # Asks the user if they want to play again, only if they have lives left
        answer = input("Do you want to roll again? Enter yes: ")

    else:
        print("You ran out of lives!")

print("GAME OVER!")
        

    



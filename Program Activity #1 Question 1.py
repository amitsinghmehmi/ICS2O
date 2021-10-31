# Author: Amit Singh Mehmi
# Date: January 18th, 2021
#
# Description: The program will take the radius of both the tent and rink from
# the user, calculate the area, and then subtract the two areas in order to
# display the amount of space or area needed to place the benches. The program
# will also display an error if the tent's radius is smaller than the rink's.

import math         # Imports math module for mathematical calculations in the program

tentRadius = float(input("Enter radius of tent: "))     # Prompts the user to enter both radii
rinkRadius = float(input("Enter radius of rink: "))

if tentRadius < rinkRadius:                 # The program makes a decision; if the radius of the tent is smaller
    print("Error!")                         # print an error
else:
    tentArea = math.pi * tentRadius**2          # if the previus condition is not true the program will calculate 
    rinkArea = math.pi * rinkRadius**2          # the area of both sectors, and subtract the two
    benchArea = float(tentArea - rinkArea)
    print("You will need", benchArea, "of area to place the benches")  # The program will display the area needed
                                                                       # to place the benches                   
    

#Python program to calculate the drop chance of an item over a certain number of attempts to get it to drop.
#Author: Trixtoxia
#Date: August 21, 2021
#Copyright (C) 2021 Trixtoxia
 
#Assigning variables. First up, the chance of 1 attempt yielding item.
chance_of_1 = float(input("What is the chance of the item dropping once, as a decimal? "))
#Stupid proofing.
while chance_of_1 > 1 or chance_of_1 < 0:
        print("Chance cannot be greater than 1, or less than zero! Try again.")
        chance_of_1 = float(input("What is the chance of the item dropping once, as a decimal? "))
#Second, taking number of attempts to get the item to drop.
trials = int(input("How many times are you going to try to get it? "))
#More stupid proofing.
while (trials < 0):
    print("Answer cannot be a negative number.")
    trials = int(input("How many times are you going to try to get it? "))
#Doing the math.
result = (1 - ( ( 1 - chance_of_1) ** trials))
#Converting drop chance to percentage, and printing the result.
print(f"The probability of getting your desired drop within {trials} tries is:")
print(str(result * 100) + "%")

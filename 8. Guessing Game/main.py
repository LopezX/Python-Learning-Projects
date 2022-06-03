# Author: Xavier Lopez
# Date Started: 5/23/2022
# Date Finished: 5/23/2022

#
# Description:
# Write a Python program that will:
#   1. ask the user for two integers
#   2. computer will randomly select an integer between the two integers
#   3. prompt user to guess a number
#       a. if correct, tell them they got it correct in x tries
#       b. if too high, tell them they are too high
#       c. if too low, tell them they are too low
#

import random

L, H = input("Please enter 2 integers: ").split()
low = int(L)
high = int(H)

if low > high:
    temp = high
    high = low
    low = temp

target = random.randint(low, high)

print("")
print("I'm thinking of a number between " + str(low) + " and " + str(high))
print("")

guess = low - 1
count = 0

while guess != target:
    guess = int(input("Enter guess: "))
    count += 1
    if guess > target:
        print("Too High\n")
    elif guess < target:
        print("Too Low\n")

if count == 1:
    print("\nCorrect, it took you 1 try to guess my number.")
else:
    print("\nCorrect, it took you " + str(count) + " tries to guess my number")

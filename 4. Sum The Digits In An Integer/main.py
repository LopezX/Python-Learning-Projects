# Author: Xavier Lopez
# Date Started: 5/18/2022
# Date Finished: 5/18/2022

#
# Description:
# Take a number from the user between 0 and 9999999 (inclusive)
#   and find the sum of the integers in the number
#   (ex. the input 1234 should give the output 10)
#

num = int(input("Enter an integer between 0 and 9999999: "))
sumOfNum = 0
digit = 0

while num > 0:
    digit = num % 10
    sumOfNum += digit
    num -= digit
    num /= 10

print("The sum of the digits is " + str(round(sumOfNum)) + ".")

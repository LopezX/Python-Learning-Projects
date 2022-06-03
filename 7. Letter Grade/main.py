# Author: Xavier Lopez
# Date Started: 5/20/2022
# Date Finished: 5/20/2022

#
# Description:
# Write a Python program that will:
#   1. ask the user to enter five test scores
#   2. check to see if test scores are below 0 or greater than 100
#       a. if so, print error message
#   3. if scores are between 0 and 100 (inclusive):
#       a. report average to two decimal places
#       b. report letter grade
#       c. report min, max and median
#

print("Please Enter Five Test Scores.\n")

A, B, C, D, E = input().split()
a = float(A)
b = float(B)
c = float(C)
d = float(D)
e = float(E)

print("")

avg = (a + b + c + d + e) / 5.0
letter_grade = "F"
if (avg >= 59.5) & (avg < 69.49):
    letter_grade = "D"
elif (avg >= 69.5) & (avg < 79.49):
    letter_grade = "C"
elif (avg >= 79.5) & (avg < 89.49):
    letter_grade = "B"
elif avg >= 89.5:
    letter_grade = "A"

temp_a = a
temp_b = b
temp_c = c
temp_d = d
temp_e = e

if a < b:
    temp = temp_a
    temp_a = temp_b
    temp_b = temp
if a < c:
    temp = temp_a
    temp_a = temp_c
    temp_c = temp
if a < d:
    temp = temp_a
    temp_a = temp_d
    temp_d = temp
if a < e:
    temp = temp_a
    temp_a = temp_e
    temp_e = temp
if b < c:
    temp = temp_b
    temp_b = temp_c
    temp_c = temp
if b < d:
    temp = temp_b
    temp_b = temp_d
    temp_d = temp
if b < e:
    temp = temp_b
    temp_b = temp_e
    temp_e = temp
if c < d:
    temp = temp_c
    temp_c = temp_d
    temp_d = temp
if c < e:
    temp = temp_c
    temp_c = temp_e
    temp_e = temp
if d < e:
    temp = temp_d
    temp_d = temp_e
    temp_e = temp

min = temp_e
max = temp_a
med = temp_c

print(str('%.2f' % a) + " "
      + str('%.2f' % b) + " "
      + str('%.2f' % c) + " "
      + str('%.2f' % d) + " "
      + str('%.2f' % e))
print("")
print("Average = " + str('%.2f' % avg))
print("Grade   = " + letter_grade)
print("Min     = " + str('%.2f' % min))
print("Max     = " + str('%.2f' % max))
print("Median  = " + str('%.2f' % med))

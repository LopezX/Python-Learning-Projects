# Author: Xavier Lopez
# Date Started: 5/18/2022
# Date Finished: 5/18/2022

#
# Description:
# Write a Python program that will calculate both roots of a quadratic
#   equation given 3 inputs. If there is a negative discriminant,
#   display "NO REAL ROOTS". If two roots are the same, display one
#

from math import *

num_roots = 0
root1 = int()
root2 = int()

a = int(input(" "))
b = int(input(" "))
c = int(input(" "))

disc = pow(b, 2) - (4 * a * c)

if disc >= 0:
    root1 = (-b - sqrt(disc)) / (2 * a)
    if disc == 0:
        num_roots = 1
    else:
        num_roots = 2
        root2 = (-b + sqrt(disc)) / (2 * a)

if (num_roots > 1) & (root1 > root2):
    temp = root1
    root1 = root2
    root2 = temp

X = -b / (2 * a)
Y = (a * pow(X, 2)) + (b * X) + c

if num_roots == 0:
    print("NO REAL ROOTS (" + '%.2f' % X + ", " + '%.2f' % Y + ")")
elif num_roots == 1:
    print(('%.2f' % root1)
          + " (" + '%.2f' % X + ", " + '%.2f' % Y + ")")
else:
    print(('%.2f' % root1) + " " + ('%.2f' % root2)
          + " (" + '%.2f' % X + ", " + '%.2f' % Y + ")")

# Author: Xavier Lopez
# Date Started: 5/18/2022
# Date Finished: 5/18/2022

#
# Description:
# Write a Python program that displays two results
# of approximating PI, should look like:
#
# PI = 2.97605
# PI = 3.28374
#

pi_approx = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11)
print("PI = " + str(round(pi_approx, 5)))

pi_approx = pi_approx + (4 * 1/13)
print("PI = " + str(round(pi_approx, 5)))

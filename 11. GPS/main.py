# Author: Xavier Lopez
# Date Started: 5/24/2022
# Date Finished: 5/24/2022

#
# Description:
# Write a Python program that will:
#   1. Prompt user for a file name
#       a. Print error messages and ask again if invalid name given
#   2. Once file is opened read a line that has a command, x and y value
#       a. If the command "START" is not read, read next line
#       b. Once the command "START" is read, continue reading "DATA" commands
#            until "STOP" command is read. While "DATA" is read:
#           i. Track the total distance traveled
#          ii. Average distance from the start
#   3. Report the final location, total distance traveled, distance to start,
#        and average distance to start
#

from math import *

valid_input = False
file_name = str()

while not valid_input:
    file_name = input("Please Enter The Name Of The Data File: ")
    try:
        f = open(file_name)
        valid_input = True
    except IOError:
        print("Bad File Name.\n")

total_dist = 0.0
avg_dist_start = 0.0
count = 0

with open(file_name, 'r') as f:
    start_trip = False
    stop_trip = False
    while not stop_trip:
        data = f.readline()
        command, strX, strY = data.split()
        X = int(strX)
        Y = int(strY)
        if (command == "START") & (not start_trip):
            start_trip = True
            start_X = X
            start_Y = Y
            prev_X = X
            prev_Y = Y

        if start_trip:
            curr_X = X
            curr_Y = Y
            if (command == "DATA") | (command == "STOP"):
                dist = sqrt(pow(curr_X - prev_X, 2)
                            + pow(curr_Y - prev_Y, 2))
                total_dist += dist

                dist_start = sqrt(pow(curr_X - start_X, 2)
                                  + pow(curr_Y - start_Y, 2))
                count += 1
                avg_dist_start += dist_start

                prev_X = curr_X
                prev_Y = curr_Y

            if command == "STOP":
                stop_trip = True
                stop_X = X
                stop_Y = Y

dist_from_start = sqrt(pow(stop_X - start_X, 2) + pow(stop_Y - start_Y, 2))
avg_dist_start /= count

print("Final Location: (" + ('%.1f' % stop_X) + ", " + ('%.1f' % stop_Y) + ")")
print("Total distance traveled " + ('%.1f' % total_dist))
print("Distance to starting point " + ('%.1f' % dist_from_start))
print("Average distance to start point = " + ('%.1f' % avg_dist_start))


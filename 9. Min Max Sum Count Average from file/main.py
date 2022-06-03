# Author: Xavier Lopez
# Date Started: 5/23/2022
# Date Finished: 5/23/2022

#
# Description:
# Write a Python program that will:
#   1. Get a name of a file from the user
#   2. open the file, if not print an error message and exit program
#   3. read unknown number of integers out of the file until it reaches end
#   4. report the min, max, sum of integers, count of integers, and
#        average of the integers
#

file_name = input("Enter Data File Name: ")

try:
    with open(file_name, 'r') as f:
        min = int()
        max = int()
        sum = 0
        num = 0
        first = True

        for line in f:
            if line != "\n":
                data = int(line)
                if first:
                    min = data
                    max = data
                    first = False

                if min > data:
                    min = data

                if max < data:
                    max = data

                sum += data
                num += 1

        avg = sum / num

        print("")
        print("Min = " + str(min))
        print("Max = " + str(max))
        print("Sum = " + str(sum))
        print("Count = " + str(num))
        print("Average = " + str('%.2f' % avg))

except IOError:
    print("File Not Found.")

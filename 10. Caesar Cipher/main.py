# Author: Xavier Lopez
# Date Started: 5/23/2022
# Date Finished: 5/23/2022

#
# Description:
# Write a Python program that will:
#   1. Prompt user for a file name and for either "encrypt" or "decrypt"
#       a. Print error messages and exit if invalid inputs
#   2. Once file is opened, either:
#       a. If "encrypt" was entered, shift all characters (including
#              whitespace) 3 values to the right
#       b. If "decrypt" was entered, shift all characters (including
#              whitespace) 3 values to the left
#   3. Print text to a file named "message" and to the screen
#   4. Report the frequency of the vowels (A, E, I, O, U, Y) to the screen
#

file_name = input("Enter File Name: ")
cipher = input("Enter encrypt or decrypt: ")
print("")
valid_command = True

if (cipher != "encrypt") & (cipher != "decrypt"):
    print("Error: Bad Command.")
    valid_command = False

try:
    a_count = 0
    e_count = 0
    i_count = 0
    o_count = 0
    u_count = 0
    y_count = 0
    out_file = open("message", 'w')
    with open(file_name, 'r') as f:
        if valid_command:
            char = f.read(1)
            while char:
                if cipher == "decrypt":
                    char_num = ord(char)
                    char_num -= 3

                if cipher == "encrypt":
                    char_num = ord(char)
                    char_num += 3

                char = chr(char_num)

                if (char == "a") | (char == "A"):
                    a_count += 1
                if (char == "e") | (char == "E"):
                    e_count += 1
                if (char == "i") | (char == "I"):
                    i_count += 1
                if (char == "o") | (char == "O"):
                    o_count += 1
                if (char == "u") | (char == "U"):
                    u_count += 1
                if (char == "y") | (char == "Y"):
                    y_count += 1

                print(char, end="")
                out_file.write(char)
                char = f.read(1)

    print("")
    print("Letter Frequency")
    print("   A    " + str(a_count))
    print("   E    " + str(e_count))
    print("   I    " + str(i_count))
    print("   O    " + str(o_count))
    print("   U    " + str(u_count))
    print("   Y    " + str(y_count))

except IOError:
    print("Error: File did NOT open.")

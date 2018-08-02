# ================= Compulsory Task ==================
# Create a new Python file in this folder called “Binary.py”
# Write a program that can convert a binary number to a decimal number.
# A binary number is basically a number that is made up entirely of 0s and 1s (e.g 101101)
# You can represent any amount you would like using binary.
# Ask the user to enter a binary number and convert that number to a decimal number.
# You can visit the following site to find out how to convert from binary to decimal:
#   http://www.rapidtables.com/convert/number/how-binary-to-decimal.htm
# Print out the decimal value of the number.
# Remember to make use of the built-in functions found in the math module as well as lists.

import math

binaryString = input('\nPlease enter a Binary number:  ')
binaryDigitList = list(binaryString)
decimalDigitList = list()
counter = int(len(binaryString))
decimal = 0

while counter > 0:
    for digit in binaryString:
        counter -= 1
        if digit == "1":
            decimal = math.pow(2,counter)
            decimalDigitList.append(decimal)
        else:
            decimalDigitList.append(0)

total = sum(decimalDigitList)

print("\nThe decimal number is:  " + str(int(total)) + "\n")
# ================= Compulsory Task 1 ==================
# Create a new file called while.py
# Write a program that always asks the user to enter a number.
# When the user enters the negative number -1, the program should stop requesting the user to enter a number,
# The program must then calculate the average of the numbers entered excluding the -1.
# Make use of the while loop repetition structure to implement the program.
# Compile, save and run your file.

numInput = 0
numTotal = 0
numCounter = 0
numAverage = 0

while numInput != -1:
    numInput = int(input("please enter a number.  Enter -1 to stop this request..."))
    numTotal += numInput
    numCounter += 1

numAverage = round(((numTotal + 1) / (numCounter - 1)),2)
print("This is the average of your numbers:  " + str(numAverage))
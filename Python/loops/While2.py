# ================= Compulsory Task 2 ==================
# Modify your while.py file to do the following:
#     - Require the user to enter their name, with only a certain name being able to trigger the loop.
#     - Print out the number of tries it took the user before inputting the correct number.
#     - Add a conditional statement that will cause the user to exit the program without giving the average of the numbers entered if, they enter a certain input.
# Compile, save and run your file.


userName = str()
failedLoginCount = -1
numInput = 0
numTotal = 0
numCounter = -1
numAverage = 0

while userName != "Russell":
    userName = input("Enter your User Name:  ")
    failedLoginCount += 1

print("You tried " + str(failedLoginCount) + " times, before successful login")

while numInput != -1:
        numInput = int(input("please enter a number.  Enter -1 to stop this request..."))
        if numInput == -2:
            print("The program has been terminated")
            exit()
        else:
            numTotal += numInput
            numCounter += 1

numAverage = round(((numTotal + 1) / (numCounter)),2)
print("This is the average of your numbers:  " + str(numAverage))
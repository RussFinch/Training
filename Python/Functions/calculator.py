# ================= BONUS Optional Task ==================
# Create a new Python file in this folder called “Optional_task.py”
# Write a program that will act as a calculator.
# Create functions named addNum, subtractNum, multiplyNum and divideNum that asks the user to enter 2 numbers and adds, subtracts, multiplies or divides them respectively.
# Print out the following menu and ask the user to input a number that corresponds to the option they would like to choose:
#       Option 1 - add
#       Option 2 - subtract
#       Option 3 - multiply
#       Option 4 - divide
# If the user enters 1 call the addNum function
# If the user enters 2 call the subtractNum function
# If the user enters 3 call the multiplyNum function
# If the user enters 4 call the divideNum function
# Make sure that the result of the caluation is printed out to the screen.

def addNum(num1, num2):
    addResult = float(num1) + float(num2)
    return addResult

def subtractNum(num1, num2):
    subResult = float(num1) - float(num2)
    return subResult

def multiplyNum(num1, num2):
    mulResult = float(num1) * float(num2)
    return mulResult

def divideNum(num1, num2):
    divResult = float(num1) / float(num2)
    return divResult

print()
print("\tOption 1 - add")
print("\tOption 2 - subtract")
print("\tOption 3 - multiply")
print("\tOption 4 - divide")
print()

response = input("Please enter option number:\t\t")
number1 = input("\nPlease enter the first number:\t\t")
number2 = input("Please enter the second number:\t\t")

if response == "1":
    print("\nYour addition result is:\t\t" + str(addNum(number1, number2)) + "\n")
elif response == "2":
    print("\nYour subtraction result is:\t\t" + str(subtractNum(number1, number2)) + "\n")
elif response == "3":
    print("\nYour multiplication result is:\t\t" + str(multiplyNum(number1, number2)) + "\n")
elif response == "4":
    print("\nYour division result is:\t\t" + str(divideNum(number1, number2)) + "\n")
else:
    print("INVALID INPUT")


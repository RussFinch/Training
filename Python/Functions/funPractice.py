# ======================= Play around with Python a bit ============================
#
#   Create a new Python file in this folder called funcpractice.py.
#   Inside it, create a function called 'addthree', that takes as input three parameters - num1, num2, num3.
#   Then, write logic to create a new variable, y, that is the sum of all three of these numbers.
#   Then, return the result y.
#   Now, after you've defined this function, write a function call to return the sum of the numbers 52, 25, and 1403.
#   Store this result in a variable called sumFunc.
#   Print out sumFunc. Don't forget to cast to a String!
#
# ==================================================================================================

def addThree(num1, num2, num3):
    total = int(num1) + int(num2) + int(num3)
    return total

a = input("Please enter a:  ")
b = input("Please enter b:  ")
c = input("Please enter c:  ")
 
print("Total equals:  " + str(addThree(a, b, c)))
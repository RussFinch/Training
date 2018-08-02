# ================= BONUS Optional Task ==================
# Create a new Python file in this folder called “Optional_task.py” 
# Use raw input to get any two numbers from the user.
# Store these numbers in variables called num1 and num2.
# Now swap the these two numbers around.
# The number stored in num1 should now be stored in num2, and the number stored in num2 should now be stored in num1.
# Print out the values of num1 and num2 before the swap, and the values of num1 and num2 after the swap.

num1 = input("Please enter your first number: ")
num2 = input("Please enter your second number: ")

print(num1 + "    " + num2)

num3 = num1
num1 = num2
num2 = num3

print(num1 + "    " + num2)

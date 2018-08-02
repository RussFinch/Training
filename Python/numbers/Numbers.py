# ================= Compulsory Exercise 1 ==================
# Create a new Python file in this folder called “Numbers.py.” 
# Ask the user to enter three different integers
# Then print out:
# - The sum of all the numbers
# - The first number minus the second number
# - The third number multiplied by the first number
# - The sum of all three numbers divided by the third number

int1 = int(input("Please enter first Integer: "))
int2 = int(input("Please enter second Integer: "))
int3 = int(input("Please enter third Integer: "))
print(int1 + int2 + int3)
print(int1 - int2)
print(int3 * int1)
print(float((int1 + int2 + int3) / int3))
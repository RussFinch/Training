# ================= BONUS Optional Task ==================
# Create a new Python file in this folder called “Optional_task.py” 
# Get user input a number and cast it to an int. Store it in a variable called num.
# Now, if the number is bigger than 10, use a for loop to output it as many times as its value.
# For example, if a user enters 11, the number 11 will be printed out 11 times.
# If the user enters 6 or anything less than equal to 10, the program should output "Sorry, too small".

enterNum = input("Enter a number\n")
num = int(enterNum)

if num >= 10:
    for i in range(1,(num)):
        print(num)
else:
    print("Sorry, too small.")
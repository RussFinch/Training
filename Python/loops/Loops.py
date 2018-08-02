# ================= BONUS Optional Task ==================
# Create a new Python file in this folder called “Optional_task.py”
# Create a program to check if a number inputted by the user is prime.
# A prime number is a positive integer greater than 1, whose only factors are 1 and the number itself.
# Examples of prime numbers are: 2, 3, 5, 7, etc.
# Ask the user to enter an integer.
# First check if the number is greater than 1.
# If it is greater than 1, check to see if it has any factors besides one and itself.
# i.e if there are any numbers between 2 and the number itself that can divide the number without any remainders 
# If the number is a prime number, print out the number and ' is a prime number!'
# If the number is not a prime number, print out the number and ' is not a prime number'

primeEnter = input("Please enter a positive integer to see if its prime:  ")

if int(primeEnter) >= 2:
    for p in range (2,int(primeEnter)):
        if (int(primeEnter) % p) == 0:
            print(primeEnter + " is not a prime number\n")
            break
    else:
        print(primeEnter + " is a prime number!\n")
else:
    print(primeEnter + " is not a prime number\n")

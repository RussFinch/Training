# ================= BONUS Optional Task ==================
# Create a new Python file in this folder called “Optional_task.py.”
# Write a program with two compilation errors, a runtime error and a logical error.
# Next to each error, add a comment that explains what type of error it is and why it occurs.

primeEnter = Input("Please enter a positive integer to see if its prime:  ")  #compilation/sytax error - input has a capital
errorValue = int(primeEnter) / 0  #The division by 0 should create a runtime error

if int(primeEnter) >= 2  #compilation/sytax error - : missing
    for p in range (2,int(primeEnter)):
        if (p % int(primeEnter)) == 0: #logical error - p % int(primeEnter) should be reversed
            print(primeEnter + " is not a prime number\n")
            break
    else:
        print(primeEnter + " is a prime number!\n")
else:
    print(primeEnter + " is not a prime number\n")
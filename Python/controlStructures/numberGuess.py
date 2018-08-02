# ================= BONUS Optional Task ==================
# Create a new Python file in this folder called “Optional_task.py”
# Create a program that allows the user to play the lottery.
# Generate a random two digit number (between 10 and 99) this number will be the lottery number.
# Ask the user to enter any two digit number this will be the user's guess.
# Get first and second digit from the two digit lottery number.
# Get the first and second digit from the user's guess.
# Print out the generated lottery number.
# If the user's guess matches the lottery number exactly, print out "Congratulations you have an exact match, you win R10 000.00"
# (i.e. if the user enters 12 and the lottery number is 12)
# If the user's guess matches the lottery numbers, but are in the wrong order print out "Congratulations you have all digits, you win R5 000.00"
# (i.e. if the user enters 48 and the lottery number is 84)
# If the user guesses one digit correctly print out "Congratulations you have one correct digit, you win R1 000.00"
# (i.e. if the user enters 27 and the lottery number is 78)
# Else print out "Sorry no match"
# To get more information on how to generate a random number vist: https://docs.python.org/2/library/random.html

import random

guess = input("\nPlease enter a 2 digit number (10-99):  ")
random = str(random.randint(10,99))
# random = input("Enter random number...")
guessChar1 = guess[0]
guessChar2 = guess[1]
randomChar1 = random[0]
randomChar2 = random[1]

print("This is your random number:  " + random + "\n")

if guess == random:
    print("Congratulations you have an exact match, you win R10,000.00\n")
elif (guessChar2 + guessChar1) == random:
    print("Congratulations you have all digits correct, you win R5000.00\n")
elif randomChar1 == guessChar1:
    print("Congratulations you have one digit correct, you win R1000.00\n")
elif randomChar1 == guessChar2:
    print("Congratulations you have one digit correct, you win R1000.00\n")
elif randomChar2 == guessChar1:
    print("Congratulations you have one digit correct, you win R1000.00\n")
elif randomChar2 == guessChar2:
    print("Congratulations you have one digit correct, you win R1000.00\n")
else:
    print("Sorry, no match\n")

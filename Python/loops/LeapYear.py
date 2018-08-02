# ================= Compulsory Task 2 ==================
# A simple rule to determine a whether a year is a leap year is to test whether it is a multiple of 4.
# Write a program to input a year and a number of years.
# Then determine and display which of those years were or will be leap years.
# Example:
# What year do you want to start with?           1994
# How many years do you want to check?           8

# 1994 isn’t a leap year
# 1995 isn’t a leap year
# 1996 is a leap year
# 1997 isn’t a leap year
# 1998 isn’t a leap year
# 1999 isn’t a leap year
# 2000 is a leap year
# 2001 isn’t a leap year

# Compile, save and run your file.

year = int(input("Please enter the year to start from:  "))
numYear = int(input("Please enter the number of years you want to check:  "))

for i in range(year,(year + (numYear))):
    if i % 4 == 0:
        print(str(i) + " is a leap year")
    if i % 4 != 0:
        print(str(i) + " isn't a leap year")
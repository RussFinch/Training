

# ================= Compulsory Task ==================
# Create a new Python file in this folder called "InvestmentCalculator.py".
# At the top of the file include the line:
#   import math
# Ask the user to input:
#   The amount that they are depositing, stored as ‘P’.
#   The interest rate (as a percentage), stored as ‘i’.
#   The number of years of the investment. stored as ‘t’.
#   Then ask the user to input whether they want “simple” or “compound” interest, and store this in a variable called ‘interest’.
# Only the number of the interest rate should be entered - don’t worry about having to deal with the added ‘%’,
# e.g. The user should enter 8 and not 8%.
# Depending on whether they typed “simple” or “compound”, output the appropriate amount that they will get after the given period at the interest rate.
# Print out the answer!
# Try enter 20 years and 8 (%) and see what a difference there is depending on the type of interest rate!

import math

P = input("Please enter the amount you are depositing:  ")
i = input("Please enter the interest rate:  ")
t = input("Please enter the number of years for investment:  ")
interest = input("Do you want to calculate simple or compund interest?  simple/compund:  ")
simpleValue = float(P) * (1+(float(i)/100)*int(t))
compoundValue = (float(P) * (math.pow(1+(float(i)/100),int(t))))

if interest == "simple":
    print("\nThe value of your simple investment after your selected period is: R" + str(simpleValue))
else:
    print("\nThe value of your compund investment after your selected period is: R" + str(compoundValue))

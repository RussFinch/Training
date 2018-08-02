#  ========== Compulsory Task ==========

# One of the most important patterns in computers and on the internet is yourpassword.
# For a password to be classified as ”Strong” the password needs to be structured in a
# certain way.  Password Strength is determined by:
# ○     The length of the password (at least 6 characters) (haveLength)
# ○     Needs to contain uppercase letters (upCase)
# ○     Needs to contain lowercase letters (lowCase)
# ○     Needs to contain numbers (haveNum)
# 
# ●  Declare boolean variables for each one of these characteristics.
# ●  You will find the name of the variable next to the condition above, they must all be initialised as false.
# ●  Then ask the user a series of yes or no questions for each variable, change the
#    boolean variable to True based on their answer.
# ●  Once 3 of the characteristics are met (3 of the variables == True) then display a message saying 
#    this is a suitable password.

haveLength = False
upCase = False
lowCase = False
haveNum = False
strength = 0

isLength = int(input("How many characters are there is your password?: "))
isUpCase = int(input("How many Upper case characters are in your password: "))
isLowCase = int(input("How many Lower case characters are in your password: "))
isNum = int(input("How many Numeric characters are there in your password: "))

# Calculate which password criteria have been met.

if isLength >= 6:
    haveLength = True
if isUpCase >= 1:
    upCase = True
if isLowCase >= 1:
    lowCase = True
if isNum >= 1:
    haveNum = True

# Update strength criterion and print results of checking.
if haveLength == True:
    print("\nYour password meets strong password Length criteria")
    strength +=1
if upCase == True:
    print("\nYour password meets strong password Upper Case character criteria")
    strength +=1
if lowCase == True:
    print("\nYour password meets strong password Upper Case character criteria")
    strength +=1
if haveNum == True:
    print("\nYour password meets strong password Numerical character criteria")
    strength +=1

# Output final result and weaknesses to be resolved.

if strength >= 3:
    print("\nGREAT! Your Password is strong enough.\n" )
if strength < 3:
    print("\nNAUGTHY!! Please fix up your password...\n")
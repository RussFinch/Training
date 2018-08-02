# ================= Compulsory Task ==================
# Create a Python file called “Control.py” in this folder.
# This is going to expand on the first control structure task we created.
# Write code to take in a user’s age using raw_input and store their age in an integer variable called age.
# Then check if the user’s age is over 18. If the user is over 18, print out the message “You are old enough!”
# else if they are over 16 print “Almost there”,
# otherwise print “You’re just too young!” You should use one if, one elif and one else statement to do this.

age = int(input("Please enter your age:  "))

if age > 18:
    print("You are old enough!")
elif age >= 16:
    print("Almost there...")
else:
    print("You're just too young!")

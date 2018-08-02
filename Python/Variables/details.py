# ================= Compulsory Task 2 ==================
# Create a new Python file in this folder called “details.py” 
# Use a Raw Input to get the following information from the user.
#   - Name
#   - Age
#   - House number
#   - Street name
# Print out a single sentence with the containing all the details of the user.  
# For example: 
#   This is John Smith he is 28 years old and lives at house number 42 on Hamilton Street.

name = input("Please enter your name: ")
age = input("Please enter your age: ")
houseNumber = input("Please enter your house number: ")
streetName = input("Please enter your street name: ")

print("This is " + name + " he is " + age + " years old and lives at house number " 
        + houseNumber + " on " + streetName + ".")
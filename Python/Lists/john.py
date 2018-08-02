# ================= Compulsory Task ==================
# Once you have read and completely understood ​example.py, ​write a Python program that takes in a user input as a String.
# While the String is not “John”, add every String entered to a  list until “John” is entered.
# Then print out the list.
# This program basically stores all incorrectly entered Strings in a list where “John” is the only correct String.
# Save this program as '​John.py' ​in this folder.
# Example program run (what should show up in the Python Console when you run it):
#       Enter your name : <user enters Tim>  
#       Enter your name : <user enters Mark>  
#       Enter your name: <user enters John>  
#       Incorrect names: [‘Tim’, ‘Mark’]

namesList = list()

while True:
    name = input("Enter your name:  ")
    if name != "John":
        namesList.append(name)
    else:
        break

print("incorrect names:  " + str(namesList))
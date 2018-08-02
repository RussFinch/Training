# ================= BONUS Optional Task ==================
# Edit the above program to allow the user to enter an integer before they enter the name.
# This  integer defines how many ‘tries’ the user will get to enter the right name.
# If the user exceeds the number of tries, the program must stop. 


namesList = list()
counter = 0

while counter <= 3:
    name = input("Enter your name:  ")
    counter += 1
    if name != "John":
        namesList.append(name)
    else:
        break

print("incorrect names:  " + str(namesList))
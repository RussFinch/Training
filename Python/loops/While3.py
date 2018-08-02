# ================= BONUS Optional Task  ==================
# Create a new file in this folder called Optional_task.py
# Ask the user to enter a number less than 100.
# If they enter one above 100, ask them to try again (and continue to do so until they follow instructions).
# Once they have entered a valid number, check if it is even and if it is then multiply it by 2 and print it out.
# If it isn't, then multiply it by 3 and print it out.

num = 0
evenNumOutput = 0
oddNumOutput = 0

num = int(input("Enter a number less than 100:  "))

while num >= 100:
    num = int(input("Enter a number LESS than 100:  "))  
if num <= 100 and num % 2 == 0:
    evenNumOutput = num * 2
    print(evenNumOutput)
else:
    oddNumOutput = num * 3
    print(oddNumOutput)

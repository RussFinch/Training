# ================= Compulsory Task ==================
# We will write a program that allows students to register for an exam venue.
# First ask the user how many students are registering.
# Create a for loop that runs for that amount of students
# Each loop asks for the student to enter their ID numbers.
# Write each of the ID numbers to a Text File called “RegForm.txt”
# This will be used as an attendance register that they will sign when they arrive at the exam venue

outFile = open('RegForm.txt', 'w')
studentNum = input("How many students are to be registered?\t")
studentID = ""

for students in range (0, (int(studentNum))):
     studentID += input("Please enter your Student ID:\t")
     studentID += "\n"

outFile.write(studentID)
outFile.close()





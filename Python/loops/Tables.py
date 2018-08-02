# ================= Compulsory Task 1  =================
# Save your program as "tables.py".
# This program needs to display the timetables for any number.
# For example, say the user enters 6 the program must print:
                       
#               The 6 times table is:
#		6 x 1 = 6
#		6 x 2 = 12
#                   …
#		6 x 12 = 72     
# Compile, save and run your file.

table = int(input("Please enter times table value:  "))

for i in range (1,12):
    print(i * table)

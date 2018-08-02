# ================= Compulsory Task ==================
# Write a program that reads the data from the text file called DOB.txt and prints it out in two different sections in the format displayed below:
# Name                 
#       1. A Masinga           
#       Etc.
# Birth date
#       1. 21 July 1988
#       Etc.

count = 0
nameList = ""
dateList = ""

f = open('DOB.txt', 'r')

for line in f:
    count += 1
    firstName, surName, bDay, bMonth, bYear = line.split(" ")
    nameList += ("\n" + str(count) + ".\t" + firstName[0] + " " + surName)
    dateList += (str(count) + ".\t" + bDay + " " + bMonth + " " + bYear)

f.close()

print("Name\n")
print(nameList)
print("\nBirth Date\n")
print(dateList)
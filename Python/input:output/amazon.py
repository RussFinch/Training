# ================= Compulsory Task  ==================

# After you've read and understand all of example.py, create a new Python file called amazon.py inside this folder.
# This programming problem is one posed to new software developer applicants to Amazon, the software development company you've probably bought a book or dvd from once in your life.
# Inside amazon.py, write Python code to read in the contents of the textfile 'input.txt', and for each line in input.txt.
# Write out a new line in a new text file output.txt that computes the answer to some operation on a list of numbers.

# If the input.txt file has the following:
#    min: 1,2,3,5,6
#    max: 1,2,3,5,6
#    avg: 1,2,3,5,6

# Your program should generate an output.txt file as following:


#    The min of [1, 2, 3, 5, 6] is 1
#    The max of [1, 2, 3, 5, 6] is 6
#    The avg of [1, 2, 3, 5, 6] is 3.4


# Assume that the only operations given in the input file are 'min', 'max' and 'avg', and that the operation is always followed by a list of comma separated integers. 
# Your program should handle any combination of operations, any lengths of input numbers. You can assume that the list of input numbers are always valid ints, and is never empty. 

lineContent = list()
strMin = str()
strMax = str()
strAvg = str()
output = str()


inFile = open('input.txt', 'r')
for line in inFile:
        parts = line[0:-1].split(':')
        lineContent = parts[1].split(',')
        operation = parts[0]
        if operation == str("min"):
            strMin = str("The min of " + str(lineContent) + " is " + min(lineContent) + "\n")
        elif operation == str("max"):
            strMax = str("The max of " + str(lineContent) + " is " + max(lineContent) + "\n")
        elif operation == str("avg"):
            average = (sum(int(i) for i in lineContent) / len(lineContent))
            strAvg = str("The avg of " + str(lineContent) + " is " + str(average))

inFile.close()

output = (strMin + strMax + strAvg)

outInsert = open('output.txt', 'w')
outInsert.write(output)
outInsert.close()
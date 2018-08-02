# ================= BONUS Optional Task ==================

# Change your program to also handle the operation 'px' where x is a number from 10 to 90 and defines the x percentile of the list of numbers. For example:

# input.txt:
#    min: 1,2,3,5,6
#    max: 1,2,3,5,6
#    avg: 1,2,3,5,6
#    p90: 1,2,3,4,5,6,7,8,9,10
#    sum: 1,2,3,5,6
#    min: 1,5,6,14,24
#    max: 2,3,9
#    p70: 1,2,3

# Your output.txt should read:
#    The min of [1, 2, 3, 5, 6] is 1
#    The max of [1, 2, 3, 5, 6] is 6
#    The avg of [1, 2, 3, 5, 6] is 3.4
#    The 90th percentile of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] is 9
#    The sum of [1, 2, 3, 5, 6] is 17
#    The min of [1, 5, 6, 14, 24] is 1
#    The max of [2, 3, 9] is 9
#    The 70th percentile of [1, 2, 3] is 2

lineContent = list()
strMin = str()
strMax = str()
strAvg = str()
strSum = str()
strPcent = str()

outInsert = open('output.txt', 'a')
inFile = open('input.txt', 'r')
for line in inFile:
        parts = line[0:-1].split(':')
        lineContent = parts[1].split(',')
        operation = parts[0]
        if operation == str("min"):
            strMin = str("The min of " + str(lineContent) + " is " + min(lineContent) + "\n")
            outInsert.write(strMin)
        elif operation == str("max"):
            strMax = str("The max of " + str(lineContent) + " is " + max(lineContent) + "\n")
            outInsert.write(strMax)
        elif operation == str("avg"):
            average = (sum(int(i) for i in lineContent) / len(lineContent))
            strAvg = str("The avg of " + str(lineContent) + " is " + str(average) + "\n")
            outInsert.write(strAvg)
        elif operation == str("sum"):
            numSum = (sum(int(i) for i in lineContent))
            strSum = str("The sum of " + str(lineContent) + " is " + str(numSum) + "\n")
            outInsert.write(strSum)
        elif operation[0] == str("p"):
            percentileNum = int(operation[1:3])
            orgList = set(lineContent)
            calcNum = (percentileNum / 100)
            percentile = int(len(lineContent) * calcNum)
            result = lineContent[(percentile - 1)]
            strPcent = str("The " + str(percentileNum) + "th percentile of " + str(lineContent) + " is " + str(result) + "\n")
            outInsert.write(strPcent)

inFile.close()
outInsert.close()
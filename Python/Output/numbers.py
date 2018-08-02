# ================= BONUS Optional Task ==================
# Create a new Python file in this folder called “Optional_task.py”
# Create a text file called "numbers1.txt" that contains Integers which are sorted from smallest to largest.
# Create another text file called "numbers2.txt" which also contains Integers that are sorted from smallest to largest.
# Write the numbers from both files to a third file called "allNumbers.txt"
# All the numbers in "allNumbers.txt" should be sorted from smallest to largest.

numList = list()

numUp = open('numbers1.txt', 'r')
for upLine in numUp:
        numList.append(int(upLine))
numUp.close()

numDown = open('numbers2.txt', 'r')
for downLine in numDown:
        numList.append(int(downLine))
numDown.close()

numList.sort()

numInsert = open('allNumbers.txt', 'w')
numInsert.write(str(numList))
numInsert.close()
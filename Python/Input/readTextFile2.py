# ================= BONUS Optional Task ==================
# Create a new Python file in this folder called �Optional_task.py�
# Create a new text file in this folder called input.txt
# In the input.txt file enter some text, making sure it is at least a few lines long.
# Write a program the will count the number of characters, words and lines in the file.
# Your program should also count the number of vowels (a's, e's, i's, o's and u's) in the file.
# Print out your results.

numCharacters = 0
numLines = 0
numWords = 0
characters = list()
aVowel = 0
eVowel = 0
iVowel = 0
oVowel = 0
uVowel = 0

f = open('input.txt', 'r')

for line in f:
    numCharacters += len(line)
    numLines += 1
    words = line.split(" ")
    numWords += len(words)
    characters += list(line)

print("\nThe total number of characters is:\t" + str(numCharacters))
print("The total number of lines is:\t\t" + str(numLines))
print("The total number of words is:\t\t" + str(numWords))

for letter in characters:
    if letter == "a" or letter == "A":
         aVowel += 1
    if letter == "e" or letter == "E":
        eVowel += 1
    if letter == "i" or letter == "I":
        iVowel += 1
    if letter == "o" or letter == "O":
        oVowel += 1
    if letter == "u" or letter == "U":
        uVowel += 1

print("The number of letter a is:\t\t" + str(aVowel))
print("The number of letter e is:\t\t" + str(eVowel))
print("The number of letter i is:\t\t" + str(iVowel))
print("The number of letter o is:\t\t" + str(oVowel))
print("The number of letter u is:\t\t" + str(uVowel) + "\n")

# ================= BONUS Optional Task ==================
# Create a new Python file in this folder called �Optional_task.py�
# Create a program that determines whether a String is a palindrome.
# A palindrome is a string which reads the same backwards as forward.
# Some examples of palindromes are: racecar, dad, level and noon
# Ask the user to enter a word and check if that word is a palindrome.
# If it is a palindrome, print out 'Your word is a palindrome'.
# If it is not a palindrome, print out 'Your word is not a palindrome'.

word = input("please enter a word:  ")
palindrome = word[::-1]

if palindrome == word:
    print("Your word is a palindrome")
else:
    print("Your word is not a palidrome")
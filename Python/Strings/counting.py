
# ================= Compulsory Task 2 ==================
# Write a Python program called �counting.py� to count the number of characters (character frequency) in a string. 
# Store each letter followed by the number of occurrences in a list and print it out. 
# Sample String : google.com'
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

# Use count string function s.count()

string = input("Please enter a string:  ")
stringList = list(string)
frequency = set(stringList)

for letter in frequency:
    print("'" + str(letter) + "': " + str(string.count(letter)) + ", ", end="")
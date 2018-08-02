# ================= Compulsory Task 1 ==================
# Create a program  called �alternative.py� that reads in a sting and makes each alternate character an Uppercase character
# and each other alternate character a lowercase character.

text = input("Please enter a string:  ")    # User enters a string 
alternate = [" "] * len(text)               # a variable list of spaces the length of variable "text" created so altered characers can "replace" them

alternate[::2] = text[::2].upper()          # the "alternate" list is sliced and characters replaced with responding siced characters from text variable
print(alternate)
alternate[1::2] = text[1::2].lower()        # the "alternate" list is again sliced however starting from character 1 and characters replaced with responding siced characters from text variable
print(alternate)
alternate = "".join(alternate)              # the list is then joined as a string
print(alternate)                            # output printed

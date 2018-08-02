# ================= Compulsory Task 1 ==================
# Create a new Python file in this folder called comprehend.py.
# Imagine there's a really rude friend of yours, that always sends emails with all words in capital letters. 
# Your friend also doesn't know how to use a spacebar, so he separates words with the : character.
# Imagine your friend sends the message "HI:HOW:R:U:TODAY:.
# Take this message, as a String. Split it into a list of String words and make each word lowercase using a list comprehension on each element.
# Read http://stackoverflow.com/questions/6797984/how-to-convert-string-to-lowercase-in-python for information on how to make words lowercase.
# Now, edit the first and last word (i.e. the first and last element of your list) to capitalise the first letter of the sentence, and add a full stop to the end of the sentence.
# Print out this new intelligent sentence.

message = "HI:HOW:R:U:TODAY:."
splitMessage = message.split(":")
messageComp = [element.lower() for element in splitMessage]
messageComp.append(".")
messageComp[0] = "Hi"
messageComp[4] = "Today"

print(* messageComp, sep = ' ')
# ================= Compulsory Task 4 ==================
# Write a Python program called �disappear�  to strip a set of characters from a string.
# Ask the user to input a string and then ask the user which characters they would like to make disappear.                                                                                                            
# For example: The quick brown fox jumps over the lazy dog.                                                                                      
# After stripping a,e,i,o,u                                                                                                         
# Th qck brwn fx jmps vr th lzy dg. 

sentence = input("\nPlease enter a sentence:  ")
character = input("\nWhich character do you want to disappear?  ")
newSentence = sentence.replace(character, " ")
print("\n" + newSentence + "\n")

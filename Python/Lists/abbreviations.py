# ================= BONUS Optional Task ==================
# Create a new Python file in this folder called “Optional_task.py”
# Write a program that is able to give you the meaning of a given abbreviation.
# Create a dictionary that contains some abbreviations and their meanings.
# Let the abbreviation be the key and the meaning of the abbreviation be the value (e.g. ADSL: Asymmetric Digital Subscriber Line).
# Make sure that you dictionary has at least 4 abbreviations and their meanings.
# If you need ideas on some abbreviations, go to http://www.abbreviations.com/
# After you have created your dictionary add 2 more abbreviations and their meanings to it.
# Now ask the user to enter an abbreviation and check if that abbreviation is in your dictionary.
# If it is print out the abbreviation and it's meaning.
# If it is not in the dictionary, print out "Abbreviation not found"


abbreviations = {
            'ADSL': 'Assymetric Digital Subscriber Line',
            'SDSL': 'Symetric Digital Subscriber Line',
            'RAM': 'Random Access Memory',
            'ROM': 'Read Only Memory'
#            'DRaaS': 'Disaster Recovery as a Service'
#            'BaaS': 'Backup as a Service'
}

abbreviations['DRaaS'] = 'Disaster Recovery as a Service'
abbreviations['BaaS'] = 'Backup as a Service'

userInput = input('\nPlease enter an abbreviation:  ')
if userInput in abbreviations:
    answer = abbreviations[userInput]
    print(str(answer + '\n'))
else:
    print("Abbreviation not found\n")
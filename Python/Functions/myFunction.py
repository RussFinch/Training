# ================= Compulsory Task 1 ==================
# Create a Python file called “myFunction.py” in this folder.
# Create your own function that prints all the days of the week
# Create your own function that takes in a sentence and replaces every second word with the word “Hello”

def daysOfWeek():
        print("Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday")
        return

daysOfWeek()

def secondHello(sentence):
    helloSentence = list()
    for index, word in enumerate(sentence.split()):
        if index % 2 == 0:
            helloSentence.append('Hello')
        if index % 2 != 0:
            helloSentence.append(word)
    print(helloSentence)
    return

secondHello("This is a test of the sentence update.")
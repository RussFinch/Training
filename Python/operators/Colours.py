# ============ Compulsory Task ==============
# 
# Follow these steps:
# 
# ● Create a new Python file in this folder called “Colours.py.”
# ● Design a program that reads in the time in minutes for three disciplines of a triathlon
#   namely swimming, cycling and running as well as the total qualifying time for all three events.
# ● The program must calculate and display the total time taken to complete the triathlon.
#   Also display the award they will receive according to the following table based on the
#   total qualifying time the user entered. 
# 
#   == Total Time ==                 == Award ==
#   Under QT                        Provincial colours
#   Within 5 minutes of QT          Provincial Half Colours
#   Within 10 minutes of QT         Provincial Scroll 
#   10 minutes or more than QT      Provincial Certificate

swimTime = float(input("Input swimming time in minutes:  ")) 
cycleTime = float(input("Input cycling time in minutes:  ")) 
runTime = float(input("Input runtime time in minutes:  ")) 
qualifyTime = float(input("Input qualifying time in minutes:  ")) 

totalTime = (swimTime + cycleTime + runTime)

if totalTime < qualifyTime:
    print("You are awarded Provincial Colours")
elif totalTime >= qualifyTime and totalTime < (qualifyTime + 5):
    print("You are awarded Provincial Half Colours")
elif totalTime >= (qualifyTime + 5) and totalTime < (qualifyTime + 10):
    print("You are awarded Provincial Scroll")
else:
    print("You are awarded Provincial Certificate")

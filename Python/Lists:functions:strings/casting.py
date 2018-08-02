# ================= BONUS Optional Task ==================
# Let's practice some casting.
# Create a new file called "Optional_task.py". 
# Write Python code to take the name of a user's favourite restaurant and store it in a variable called 
# favRest.
# Now, below this, write a statement to take in the user's favourite number. Use casting to store it in
# a variable called intFav.
# Now print out both of these using two separate print statements below what you have written. Be careful!
# Once this is working, try cast favRest to an int. What happens? Add a comment in your code to explain why
#  this is.

FavRest = input("What is your favourite restaurant?: ")
FavNum = input("Please enter your favoutite number: ")
intFav = int(FavNum)

print(int(FavRest))
print(intFav)

# The casting of the string FavRest into an integer causes the program to fail as the letters cannot be
# cast into numbers.  However, a string of numbers can be.
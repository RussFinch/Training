# ================= Compulsory Exercise 1 ==================
# Create a new Python file in this folder called “Strings.py” 
# Declare the variable called hero = “Super Man”
# Print it out in the following way:
#   S^U^P^E^R M^A^N
# Do Not use any functions to do this

superMan = "Super Man"

superMan = str(superMan.upper())
char1 = superMan[0]
char2 = superMan[1]
char3 = superMan[2]
char4 = superMan[3]
char5 = superMan[4]
char8 = superMan[7]
char9 = superMan[8]

print(
    (char1) + "^" + (char2) + "^" + (char3) + "^" + (char4) + "^" 
        + (char5) + superMan[5:7] + "^" + (char8) + "^" + (char9)
    )
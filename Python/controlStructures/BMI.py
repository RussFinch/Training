# ================= BONUS Optional Task ==================
# Create a new Python file in this folder called “Optional_task.py”
# Create a program that calculates a person's BMI 
# Ask the user to enter their weight in kg and their height in m
# Use the formula below to calculate the user's BMI:
# BMI = (weight in kg) / ((height in m)*(height in m))
# If the users BMI is 30 or greater the user is obese 
# else if the users BMI is 25 or greater the user is overweight 
# else if the users BMI is 18.5 or greater the user is normal
# If the users BMI is  less than 18.5 the user is underweight 
# Display the users BMI and whether they are obese, overweight, normal or underweight 

weight = float(input("Please enter your weight in Kg:  "))
height = float(input("Please enter your height in m:  "))
BMI = round((weight / (height * height)),2)

if BMI >= 30:
    print("Your BMI is: " + str(BMI) + "\nYou are Obese!")
elif BMI >= 25:
    print("Your BMI is: " + str(BMI) + "\nYou are Overweight...")
elif BMI >= 18.5:
    print("Your BMI is: " +str(BMI) + "\nYou are normal.")
else:
    print("Your BMI is: " + str(BMI) + "\nYou are underweight.")

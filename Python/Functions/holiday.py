# ================= Compulsory Task 2 ==================
# Create a Python file called “holiday.py” in this folder.
# You will need to to create four functions:
#   - Hotel cost - This function will take the number of nights as an argument and return a total cost (You can choose the price per a night)
#   - Plane cost - This function will take the city you are flying to as an argument and return a cost for the flight (Hint: use if/else if statements in the function to retrieve a price based on the chosen city)
#   - Car rental - This function will take the number of days  as an argument and return the total cost.
#   - Holiday cost - This function will take three arguments, number of nights, city, and days.
#     Using these three arguments, you can call all three of the above functions with respective arguments and finally return a total cost for your holiday.
# Print out the value of your Holiday function to see the result!
# Try using your app with different combinations to show it’s compatibility with different options

def hotelCost(noNights):
    hotelTotal = (int(noNights) * 150)
    return hotelTotal

def planeCost(city):
    if city == 'London':
        planeTotal = 750
    elif city == 'New York':
        planeTotal = 850
    elif city == 'Mumbai':
        planeTotal = 950
    else:
        planeTotal = print("This is not a valid destination")
    return planeTotal

def carRental(days):
    carTotal = int(days) * 50
    return carTotal

def holidayCost(hotelTotal, planeTotal, carTotal):
    holidayTotal = (hotelTotal + planeTotal + carTotal)
    return holidayTotal

city = input("Where would you like to fly?  ")
hotel = input("Please enter how long you would like to stay:  ")
car = input("For how many days would you like a car?  ")
print("\nThe price of your flight is:\t" + str(planeCost(city)))
print("The price of your hotel is:\t" + str(hotelCost(hotel)))
print("The price for car hire is:\t" + str(carRental(car)))
print("\nThe total cost of you holiday:\t" + str(holidayCost(planeCost(city), hotelCost(hotel), carRental(car))) + "\n")





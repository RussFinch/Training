# ================= Compulsory Task ==================
# Create a Python file called “Courier.py” in this folder.
# You need to design a program for a courier company to calculate the cost of sending a parcel.
# Ask the user to enter the price of the package they would like to purchase.
# Ask the user to enter the total distance of the delivery in km’s.
# Now add on the delivery costs to get the final cost of the product.
# There are four categories to factor in when determining a parcel’s final cost each with two options based on their delivery preferences. (Use an if else statement based on the choice they make)
#       - Air R0.36 per Km or freight R0.25 per Km
#       - Full insurance R50 or limited insurance R25
#       - Gift R15.00 or no gift R0.00
#       - Priority R100 or standard delivery R20
# Work out the total cost of the package based on the selection in each category.

# Input Variables
packagePrice = round(float(input("Please enter the price of package you'd like to purchase: ")),2)
deliveryDistance = int(input("Please enter total distance for delivery in Km's: "))
deliveryType = input("Would you like AIR or FREIGHT delivery?:  Air/Freight: ")
insurance = input("would you like FULL or LIMITED insurance?:  Full/Limited: ")
gift = input("Is this package a gift?:  Yes/No: ")
priority = input("Is this delivery PRIORITY?:  Yes/No: ")

# Cost calculation Variable
deliveryCost = 0.00
additionalCost = 0.00

# IF ELSE statements for cost calculation
if deliveryType == "Air":
    deliveryCost += ((0.36 * deliveryDistance) + packagePrice)
else:
    deliveryCost += ((0.25 * deliveryDistance) + packagePrice)

if insurance == "Full":
    additionalCost += 50.00
    print("The price for FULL insurance is: R50.00")
else:
    additionalCost += 25.00
    print("The price for LIMITED insurance is: R25.00")

if gift == "Yes":
    additionalCost += 15.00
    print("The cost of gift wrapping is an additional R15.00")

if priority == "Yes":
    additionalCost += 100.00
    print("Priority delivery price is: R100.00")
else:
    additionalCost += 20.00
    print("Standard delivery price is: R20.00")

totalCost = (deliveryCost + additionalCost)

# Programme Output
print("\nPackage price plus Delivery is: R" + str(round(deliveryCost,2)) + "")
print("\nThe TOTAL price to send your parcel is: R" + str(round(totalCost,2)) + "\n")

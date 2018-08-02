# ================= Compulsory Exercise 2 ==================
# Create a new Python file in this folder called “Shopping.py.” 
# Once this is done ask the user to enter the name of three products
# The price of each product. Each product must have two decimal values.
# Calculate the total of all three products.
# Calculate the average price of the three products.
# Then print out the following sentence after performing your calculations:
#	“The Total of [product1], [product2], [product3] is Rxx,xx and the average price of the items are Rxx,xx.”

prod1 = input("Please enter name of Product 1: ")
prod1Price = float(input("and its price: "))
prod2 = input("Please enter name of Product 2: ")
prod2Price = float(input("and its price: "))
prod3 = input("Please enter name of Product 3: ")
prod3Price = float(input("and its price: "))

total = float(prod1Price + prod2Price + prod3Price)
average = float((prod1Price + prod2Price + prod3Price) / 3)

print("The Total of " + prod1 + ", " + prod2 + ", " + prod3 + " is R" + str(total) + " and the average price of the items is R" + str(round(average,2)))

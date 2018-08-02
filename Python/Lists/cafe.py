#*******************  Compulsory Task **********************

# Create a new Python file in this folder called cafe.py.

# Create a list called menu, which should contain at least
# 4 items in the cafe.
# Next, create a dictionary called stock, which should contain
# the stock value for each item on your menu.

# Create another dictionary called price, which should contain 
# the prices for each item on your menu.

# Next, create a function which will calculate the total stock
# worth in the cafe.

# You will need to remember to loop through the appropriate 
# dictionaries and lists to do this.

# Finally, print out the result of your function.


menu = ['cake', 'coffee', 'tea', 'sandwiches']

stock = {
    'cake': 10,
    'coffee': 100,
    'tea': 75,
    'sandwiches': 15,
}

price = {
    'cake': 3.50,
    'coffee': 3.00,
    'tea': 2.50,
    'sandwiches': 5.00,
}

value = 0

for x in stock and price:
    value += (price[x] * stock[x])

print(value)


# This coding language is Python!
# How can we represent our to-dos on a computer?

todos = ["brush teeth", "make bed", "grab a coffee"]

# We can check our list by printing it!
print(todos) # ['brush teeth', 'make bed', 'grab a coffee']

# What if we want to check a specific todo we must complete?
# What do we do need to do first in the morning?
print(todos[1]) 

# Nope!!! What will this print? 
# It prints "make bed" !!!!

# Arrays actually start counting with 0!

# To get "brush teeth" we use this index of 0.
print(todos[0]) # brush teeth
print(todos[1]) # make bed
print(todos[2]) # grab a coffee

# If we do todos[3] we will get an "out of index" error!
# This means that our list does not have that item!
# Out of index is a super common error, be cautious of it!

# How do we add to our array?
# What if we need to also need to feed our cats in the morning?
todos.append("Feed the cats")

# Let's check if it worked!
print(todos) 
# ['brush teeth', 'make bed', 'grab a coffee', 'Feed the cats']

# What if we complete a todo item?
# How do we remove something from an array?
todos.remove("Feed the cats")

# Check
print(todos) # ['brush teeth', 'make bed', 'grab a coffee']

# Or delete at a certain index:
del todos[0]

# Check
print(todos) # ['make bed', 'grab a coffee']



# Resetting our array (or comment out the prior lines)
todos = ["brush teeth", "make bed", "grab a coffee"]

# Challenge: what if we need to "Feed the cats" before getting coffee?
# We can use the insert function and choose the index!
# To make the item 3rd in our list, use index 2 (since we start at 0)!
todos.insert(2, "Feed the cats")

# Check
print(todos) # ['brush teeth', 'make bed', 'Feed the cats', 'grab a coffee']

# Fun fact: Python allows us to combine data types
# Although I do not recommend it!
test = [1, "hello", 3.14]
print(test)

# NEXT CONCEPT: Functions

# Example: y = 2x 

def doubleNumber (x): 
    return 2 * x

# x is our input, and we "return" our output

# Let's test our function!
print(doubleNumber(2)) # 4

# Coffee Function

def getCoffee (order):
    return ("Here's your " + order)

print(getCoffee("Vanilla Latte")) # Here's your Vanilla Latte

# Challenge: What if you order multiple coffees?

def getMultipleCoffees(listOfOrders):
    listOfCompletedCoffees = []
    for coffee in listOfOrders:
        listOfCompletedCoffees.append(coffee + " is done!")
    return listOfCompletedCoffees

# Test the code: Pass in an array as your input!
print (getMultipleCoffees(["Vanilla Latte", "Cold Brew", "Mocha"]))
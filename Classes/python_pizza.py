print("Thank you for choosing Python Pizza Deliveries!")
size = input("#What size pizza do you want? S, M, or L =>")
add_pepperoni = input("# Do you want pepperoni? Y or N =>")
extra_cheese = input("# Do you want extra cheese? Y or N =>")

#Creating Variables to process the correct price.
bill = 0
pepperoni = 0
cheese = 0

# Check if Cheese was added
if (extra_cheese == "Y"):
    cheese = 1

# Check if Pepperoni was added or not.
if (add_pepperoni == "Y"):
    if (size != "S"):
        pepperoni = 3
    else:
        pepperoni = 2
else:
    pepperoni = 0

# Calculating Pizza Value by Its Size.
if (size == "S"):
    bill = 15 + pepperoni + cheese
elif (size == "M"):
    bill = 20 + pepperoni + cheese
else:
    bill = 25 + pepperoni + cheese

print(f"Your final bill is: ${bill}.")
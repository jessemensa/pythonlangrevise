# Creating an order 

import burger 

BURGER_PRICE = 6.00 
BURGER_CONDIMENTS = ["tomato", "lettuce", "onion", "cheese"]

DRINK_TYPES = ["fanta", "coke", "sprite"]
DRINK_SIZES = [12, 16, 20]
DRINK_PRICES = [1.00, 2.00, 3.00]

SIDE_PRICE = 3.00 
SIDES = ["fries", "coleslaw", "salad"]

COMBO_DISCOUNT = 2.00

# GETTING A BURGER ORDER 
def get_burger_order():
    b = burger("Burger",BURGER_PRICE)
    q1 = input("Do you want any condiments on your burger? (y for yes)")
    if q1.lower() == "y":
        for condiment in BURGER_CONDIMENTS: 
            q = input("Do you want " + str(condiment) + "? (y for yes)")
            if q.lower() == "y": 
                b.add_condiment(condiment)
    return b 

def get_drink_order():
    print("These are available drinks")
    print(DRINK_TYPES)
    print("These are the available sizes:") 
    print(DRINK_SIZES)
    choice = False
    drink_name = None
    drink_size = None
    drink_price = None
    while choice == False:
        q1 = input("What drink do you want? ")
        if q1.lower() in DRINK_TYPES:
            choice = True 
            drink_name = q1.lower() 
        else:
            print("Please enter a valid drink")

    choice = False 
    while choice == False:
        q1 = input("What size do you want? " + str(DRINK_SIZES) + ": ")
        if int(q1) in DRINK_SIZES:
            choice = True 
            drink_size = int(q1) 
        else:
            print('Please enter a valid size')
    drink_price = DRINK_PRICES[DRINK_PRICES.index(drink_size)]
    d = drink(drink_name, drink_size, drink_price)
    return d 


def order_once():
    possible_options = [1, 2, 3, 4]
    print("Type 1 for a burger ") 
    print("Type 2 for a drink")
    print("Type 3 for a side drink")
    print("Type 4 for a combo")
    choice = None 
    while choice == None: 
        q1 = input("Please enter your choice: ")
        if int(q1) in possible_options: choice = int(q1) 
    item = None 
    if item == 1: 
        item = get_burger_order()
    elif choice == 2: 
        item = get_drink_order() 
    elif choice == 3: 
        item = get_side_order() 
    elif choice == 4: 
        item = get_combo_order() 
    return item 



def order_many():
    print("Welcome to Jesses Burger Shop?? ")
    q1 = input("May i have your order please?? ")
    o = order(q1) 
    print("Lets begin your order in!")
    done = False 
    while done == False: 
        item = order_once() 
        o.add_item(item) 
        q1 = input("Do you need more items? (Enter n to stop.) ")
        if q1.lower() == "n": 
            done = True 
    return o 

def get_side_order():
    print('These are the available sides')
    print(SIDES) 
    choice = False 
    side_name = None 
    while choice == False:
        q1 = input("How many sides do you want")
        if q1.lower() in SIDES:
            choice == True 
            side_name = q1.lower() 
        else:
            print("Enter a valid side")
    s = side(side_name, SIDE_PRICE)
    return s 

def get_combo_order():
    print("Lets get a combo meal!")
    print("First lets order the burger for your combo")
    b = get_burger_order() 
    print("Now lets order the drink for your combo")
    d = get_drink_order() 
    print("Finally, lets order the side for your combo")
    s = get_side_order() 
    c = combo("Combo", b, d, s, COMBO_DISCOUNT) 
    return c 


# display the output 
client_order = order_many() 
client_order.display() 


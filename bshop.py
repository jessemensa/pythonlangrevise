# BUILDING A BURGER SHOP APPLICATION 

# REQUIREMENTS 
# ASK THE CUSTOMER IF THEY WANT A BURGER , SIDE , DRINK OR A COMBO 
# PROMPT THEM FOR DETAILS ABOUT THEIR SELECTION 
# CREATE THE ITEM BASED ON THEIR SELECTIONS 
# ADD THE ITEM TO THE ORDER 
# REPEAT THESE STEPS UNTIL THE CUSTOMER DOESNT WANT TO ORDER AGAIN 
# DISPLAY THE ORDER DETAILS INCLUDING THE PRICE 
# THANK THE CUSTOMER FOR THEIR BUSINESS 
# GIVE THE CUSTOMER THE OPTION TO CANCEL THEIR ORDER AT ANY POINT IN THE ORDERING PROCESS 

# THE CODE 
# GREET THE CUSTOMER AND ASK THEIR NAME 
# ASK THE CUSTOMER WHAT THEY WANT TO ORDER 
# ASK THE CUSTOMER FOR CUSTOMISATIONS IE BURGER TOPPINGS OR DRINK SIZE 
# ADD EACH ITEM TO THE ORDER AS REQUESTED 
# ASK THE CUSTOMER TO CONTINUE OR COMPLETE THEIR ORDER AFTER EACH ITEM 
# WHEN THE CUSTOMER COMPLETES THE ORDER, THE PROGRAM WILL DISPLAY THE ORDER AND THE TOTAL PRICE FOR THE ORDER 
# THE CUSTOMER IS ABLE TO ORDER A COMBINATION OF THE FOLLOWING ITEMS -> BURGER | DRINK | SIDE 


# CREATE THE CLASSES 

class food_item:
    def __init__(self, name, price):
        self.name = name 
        self.price = price 
        # creates a string representation of an object drrived from the fooditem class 
    def __str__(self):
        return "Item: " + self.name + "\n" + "Price: $" + str(self.price) + "\n" 
     # This method gets the price of the food item 
    def get_price(self): 
        return self.price 

# Create the Burger class 
class burger(food_item):
    # init calls super class method to initialise the name and price from the parent food item class 
    def __init__(self, name, price):
        super(burger, self).__init__(name, price)
        # put condiments inside a list 
        self.condiments = [] 
        # method that add condiments inside the list via membership 
    def add_condiment(self, condiment):
        if condiment not in self.condiments:
            self.condiments.append(condiment) 
    # override the string rep method 
    # Since we are inherting from base class food item, we can override some functionalities 
    # ie overriding the string representation function and customising it to our own taste 
    #  this function calls the super class method and calls the string representation method 
    # then add the statement into the new string statement and return it 
    def __str__(self):
        s = super(burger, self).__str__() 
        s = s + "Condiments: " + ", ".join(self.condiments) 
        return s 

# create the drink class 
class drink(food_item): 
    def __init__(self, name, size, price): 
        super(drink, self).__init__(name, price) 
        self.size = size 
        # same as above, override the string representation methid 
    def __str__(self):
        s = super(drink, self).__str__() 
        s = s + "Size: " + str(self.size) + "oz" 
        return s 

# create a side class 
class side(food_item):
    def __init__(self, name, price):
        super(side, self).__init__(name, price) 

# Combo class 
class combo(food_item):
    def __init__(self, name, b, d, s, discount): 
        self.name = name 
        self.burger = b
        self.drink = d 
        self.side = s 
        self.discount = discount 
        #after inheriting from the base class 
        # this here is calling all methods that inherited get price from the base class 
        # and doing some calculations on them 
        self.price = self.burger.get_price() + self.drink.get_price() + self.side.get_price() - self.discount 

# overrides the one in the base class 
    def __str__(self):
        s = "" 
        s = s + "Combo: " + self.name + "/n"
        s = s + str(self.burger) + "\n" + str(self.drink) + "\n" + str(self.side) + "\n" 
        s = s + "Combo Price Before Discount: $" + str(self.burger.get_price() + self.drink.get_price() + self.side.get_price()) + "\n"
        s = s + "Discount: $" + str(self.discount) + "\n"
        s = s + "Combo Price After Discount: $" + str(self.price) + "\n" 
        return s 

# create the order class and this doesnt inherit anything 
class order: 
    # initialisation 
    def __init__(self, name): 
        self.name = name 
        self.items = [] 
    # method to add item into the items list 
    def add_item(self, item):
        self.items.append(item) 
    # method to get price 
    # perform some iteration inside the list 
    # grab each item and and the price variable set to the getprice method and return the price 
    def get_price(self):
        price = 0.0 
        for item in self.items: 
            price = price + item.get_price() 
        return price 
   # method that returns a string representation of the order summary 
    def __str__(self):
        s = [str(item) for item in self.items] 
        return "\n".join(s) 
    def display(self):
        print("==========================================") 
        print("Here is a summary of your order") 
        print("Order for " + self.name)
        print("Here is a list of items in the order")

        for item in self.items: 
            print("=============")
            print(str(item))
        print("---------------")
        print("Total Order Amount: $" + str(self.get_price()))
        print("=============================================")

# CREATE MAIN FILE 
        
        
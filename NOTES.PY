# control statements in python 
# Math operations in python 
# Arithmetic operations 
# COMPARISON, ASSIGNMENT, LOGICAL, BITWISE, MEMBERSHIP AND IDENTITY 

# CONTROL STATEMENTS IN PYTHON 
# IN ORDER FOR A PROBLEM TO BE COMPUTABLE 
# AN ALGORITHM MUST BE CONSTRUCTED 
# INSTRUCTIONS CAN BE PRESENTED IN THREE STRUCTIURES 
# SEQUENCE 2. SELECTION 3. ITERATION 

# SEQUENTIAL FLOW OF DATA 
from posixpath import split


print(2+3) 

# sequence control structure 
# 1. prompt user to enter something 
# find the sum of that number 
# divide the sum by another number 
# sequence carries out a series of print statements 

# statement selection - if and else statements 
password = "admin" 
condition = (password == "admin") 
if condition:
    print("password correct")
else: 
    print("password incorrect")

# conditional statements 
age = 21 
condition = (age >= 16) 
if condition == True:
    print("This person is allowed to drive")
else:
    print("This person is not allowed to drive")


# nested conditions 

color = "morning"
if color == "red":
    print("The color is red")
elif color == "blue":
    print("The color is blue")
elif color == "yellow":
    print("The color is yellow")
else:
    print("Please enter the valid color")

# taking data from the user 
color = input("Please enter a color [red, green, yellow, blue, pink]: ")
if color == "red":
    print("Color is red")
elif color == "green": 
    print("The color is green")
elif color == "yellow": 
    print("The color is yellow")
elif color == "blue":
    print("The color is blue") 
else:
    print("Please enter a valid color that is not in the list")


# Logical Operations and if elif else statements 
# write a program that takes users credit score and display if 
# credit score is low, good or excellent 
#NB: range of values 
creditscore = int(input("Please tell us your credit score: "))
if creditscore <= 400:
    print("You have a low credit score")
elif creditscore <= 800 and creditscore <=600:
    print("You have a good credit score")
elif creditscore >= 800:
    print("You have an excellent credit score")
else:
    print("please enter a valid credit score between 0 and 900")

# LOOPS AND DATA STRUCTURES - ITERATION 
# FOR RUN THROUGH NUMBERS OR SOMETHING AND PRINT THEM OUT INDIVIDUALLY 
for message in range(3):
    print("Wake up", end=" ")
    print("wake up")

# WHILE LOOP, CHECK A CONDITION, RUN IT AND STOP WHEN THE STATE OF THE 
# CONDITION CHANGES. 
i = 0 
while ((i < 10) == True):
    print(i) 
    i += 1 


# write a program that collects usernames and prints them out 
# create a variable holds on to a list that will store the username 
names = [] 
# create a variable that stores user takes Yes or No 
userContinue = "" 

while userContinue != "N":
    name = input("What us your name? ")
    print("You entered: "+name) 
    names.append(name)
    userContinue = input("Continue (Y or N")
print(names) 

# Collecting a limited number of username 
names = [] 
userContinue = "" 
count = 0 

while count < 5 and userContinue != "N":
    name = input("What your name ? ")
    print("You entered: "+name)
    count += 1 
    names.append(name) 
    userContinue = input("Continue (Y or N)")
print(names) 

# checking the length of a name 
firstname = input("Please enter your first name: ")
lastname = input("Please enter your last name: ")
print(firstname, lastname) 
print(len(firstname) + len(lastname)) 


# Iterating through a string 
message = "Hello World!"

for ctr in message:
    print(ctr) 

# Iterating through employees 
employees = ["Jesse", "Mensah", "Mirek", "Deepangeli"]
for names in employees:
    print(names) 
    for names2 in names:
        print(names2.upper()) 
    print("----")

# SEVERAL DATA STRUCTURES AVAILABLE TO PYTHON DEVS 
# LIST, TUPLE, DICTIONARY, SETS, INDEX AND VARIABLES 

# LISTS 
["Jesse", "Mensah"] # List of tw names 

# take a list of employees and put them inside a list 
employeeList = [] 
number = input("Enter a number: ")
print(number) 

for num in range(0, int(number)):
    firstname = input("Enter first name: ")
    lastname = input("Enter last name: ")
    position = input("Enter position: ")
    empnum = input("Enter employee number: ")
    list_of_items = [firstname, lastname, position, empnum]
    employeeList.append(list_of_items)

for ctr in employeeList: print(*ctr, sep=", ")

# using index to get data out of a list 
customer_details = ["Jesse", "Sheriff", "Caleb", "Louisa"]
name = customer_details[0] 
print(name) 
print(customer_details[-1])


# Slicing data [start: stop: step] 
firstList = list(range(1, 11)) 
print(firstList)
slicedList = firstList[2:6] 
print(slicedList) 



# Tuples -> another way to save a group of related data in python 
# Tuple vs List -> Tuple is immutable and cannot be changed. 
age_range = (18, 120) 
print(age_range) 
print(type(age_range))

info = ("Maria", "Smith", 33)
print(info) 

# with tuple u cant do a lot of manipulation with it just accessing 
# data from it 
# tuples do not support append, insert, remove method, pop method and del method 


# CONCATENATING TUPLES 
tuple_of_names_1 = ("Jesse", "Mensah")
print(tuple_of_names_1)

tuple_of_names_2 = ("Amoako", "Kofi")
print(tuple_of_names_2)

tuple_of_names = tuple_of_names_1 + tuple_of_names_2 
print(tuple_of_names) 

# ITERATING AND SEARCHING THROUGH A TUPLE 
tuplenames = ("Belinda", "Ekow", "Sheriff", "Mensah", "Jesse")
search_term = "Ekow" 

# membership 
if search_term in tuplenames: 
    print(search_term + " appears at least once in the tuple")

for name in tuplenames:
    if name == search_term:
        print("we found " + search_term)


# DICTIONARIES -> stores data in key value pairs 
accounts_dict = dict() 
accounts_dict[1] = "Jesse"
accounts_dict[2] = "Mensah" 
print(accounts_dict) 

# also create a dictionary in one step 
myFirstDict = {
    "brand": "Mercedes", 
    "model": "GLE", 
    "year": 2021, 
}
print(myFirstDict) 

# Iterating through a dictionary to get the keys 
for keys in myFirstDict.keys():
    print(myFirstDict[keys]) 

# Iterating through a dictionary to get the values 
for vals in myFirstDict.values():
    print(myFirstDict[vals]) 


# printing and summing a variable number of items 
yearly_revenue = {
    2017: 10000, 2018: 20000, 2019: 120000
}

total_income = 0; 
for year in yearly_revenue.keys(): 
    total_income += yearly_revenue[year]
    print(year, yearly_revenue[year])
print(total_income)
print(total_income/len(yearly_revenue))

# Items() method 
students_dict = dict() 
students_dict['X10000'] = 'Michael'
students_dict['X10002'] = 'Nia'
for key, value in students_dict.items(): 
    print(key) 
    print(value) 

# checking for the existence of a key 
# use if statement for check for membership 


# SETS -> STORE, RETRIEVE AND MANIPULATE DATA INSIDE A SET 
# ITERATE THROUGH A SET 
# CHECKING FOR MEMBERSHIPS 
# REMOVING ITEMS FROM A SET 
# WORK WITH MULTIPLE SETS TO DETERMINE DIFFERENCES INCLUDING INTERSECTIONS, UNIONS AND 
# SET -> UNORDERED AND UNINDEXED COLLECTION OF UNIQUE VALUES 
names = {"Robert", "Mark", "Nancy"}
print(names) 

# Banking terms in a set 
banking_products = {"savings", "current", "treasurybills"}
print(banking_products) 

# retrieve items from a list 
for products in banking_products:
    print(products) 
# add items to a list 
banking_products.add("bonds")


# UNIQUNESS OF A SET 
# each item in a set must be unique within that set 
# duplicate items will be ignored

# Adding duplicates to a set , dont work with sets as it does with lists 
# Memberships in sets 
print("savings" in banking_products)

# searching for items in a set 
currentlist = {
    "Jesse", 
    "Simon", 
    "Michael", 
    "Anderson"
}
print(currentlist) 
lower_list = [x.lower() for x in currentlist] 
if input("Enter the name: ").lower() in lower_list:
    print("The student name matches the name you entered")
else:
    print("The name did not match any in our customer list")

# Calculating the length of a set 
food = {"pasta", "burger", "hot dog", "pizza"}
print(food) 
print(len(food)) 

# checking the length of a set 
user_names = set() 
integer = int(input("Please enter an integer for the number of usernames you would enter: "))
while len(user_names) < integer: 
    user_name = {input("Please enter a username: ")}
    user_names.update(user_name) 
print(user_names)

# Deleting items from a list is as simple as remove and discard 
# Clear method -> want to completely update an existing set with new data 

# prompt for input 
useraddress = input("Enter an address: ")
if useraddress.strip(): 
    print("Your address is " + useraddress) 
    split_address = useraddress.split() 
    print(split_address)
    # now lets display only the house number
    print(split_address[0])
    # make it cleaner 
    print("Your house number is " + split_address[0])
    # display the street name 
    print("Your street is " + "".join(split_address[1:])+".")

# FUNCTIONS 
def add(firstnumber, secondnumber):
    return firstnumber + secondnumber
sum1 = add(1, 10) 
sum2 = add(3, 12) 
print(sum1) 

# write a function that finds numbers greater than 5 and 0 
# using membership and for loop 
def find(numbers, thresholdvalue): 
    for num in numbers:
        if num > thresholdvalue: 
            print(num) 
numbers = [1, 5, 10, 100, 0, -1] 
print(find[numbers, 5])


# create a function to find the numbers divisible by a factor 
def find_div(numbers, factor): 
    for num in numbers: 
        if num % factor == 0: 
            print(num) 

# now call the function and use it 


# Function that checks transaction limit in a banking database 
def check_transactionlimit(amount):
    if amount > 10000:
        print("Above maximum transaction limit")
    else:
        print("Transaction is within the limit")

# DEFAULT INPUT VALUES 
def display(message="Hello Customer"):
    print(str(message))

display("Hello World")
display() 
display(True) 


# Order matters with default parameters 
# this throws an error bcos parameter with default value precedes parameter without 
# default value 
def display1(message1, message2 = "Hello World"): 
    print(str(message1) + str(message2))

# Investigate this issue 
def display2(message1 = "Hello World", message2):
    print(str(message1) + str(message2))

# Arbitrary arguments 
def realFunction(fname, lname):
    print(fname + " " + lname) 
# call the function 

# Variable amount of information passed to a function 
def display_customer_input(*argv): 
    for arg in argv: 
        print(arg) 

customer_1 = ["Jesse", "Mensah", "Kwame"]
print(display_customer_input(*customer_1)) 

# Function to complete the sum of a variable number 
def compute_sum(*numbers): 
    total = 0 
    for n in numbers: 
        total += n 
    return total 

numbers = 1, 5, 5, 7, 10, 1 
summation = compute_sum(*numbers) 
print(summation) 


# Keyword arguments 
def my_function(fam1, fam2, fam3):
    print("The youngest family member is " + fam2) 

my_function(fam1="Jesse", fam2="Mensah", fam3="Jessica")

# arbitrary keyword arguments 
def my_function(**family):
    print("Her last name is " + family["lname"])

my_function(fname = "Jesse", lname = "Mensah")


# The display function 
def display(**kwargs):
    for keyword, value in kwargs.items():
        print(keyword + ": " + value) 

display(first_name = "Jesse", last_name="Mensah")
display(name="Jesse", age="33", location="Ghana")



# Object Oriented Programming in Python 
class Person: 
    def __init__(self, name):
        self.name = name 
        

p = Person("Jesse")
print(p.name) 

# Multiple attributes 
class FullPerson: 
    def __init__(self, firstname, lastname):
        self.firstname = firstname 
        self.lastname = lastname 

person1 = FullPerson("Jesse", "Mensah")
print(person1.lastname) 


# Working with Methods 
# Data and Functionalities can be bundled together in Python 

class Human: 
    def __init__(self, firstname, lastname):
        self.firstname = firstname 
        self.lastname = lastname 

    def displayinfo(self):
        print("Person firstname: " + self.firstname) 
        print("Person lastname: " + self.lastname)

person1 = Human("Jesse", "Mensah")
print(person1.displayinfo()) # this calls the method to display the name 


# Simple Banking App in Python 
class BankCustomer: 
    def __init__(self, cust_id, firstname, lastname): 
        self.customerid = cust_id 
        self.firstname = firstname 
        self.lastname = lastname 

    # method that displays customers details 
    def displaycustomerinfo(self): 
        print("Customer first name is: " + self.firstname)
        print("Customers last name is: " + self.lastname) 
        print("Customer id is: " + self.customerid)

class BankAccount: 
    def __init__(self, acc_id, accountname, accountType):
        self.accountid = acc_id
        self.accountname = accountname
        self.accountType = accountType

    def displayaccountinfo(self):
        print("The account name is " + self.accountname)
        print("The account type is " + self.accountType)
        print("The account id is " + self.accountid)

# set up first customer 
customer1 = BankCustomer(10003, "Jesse", "Mensah")
customer2 = BankCustomer(10005, "Jessica", "Mensah")
customer3 = BankCustomer(10006, "Jasmine", "Mensah")

account1 = BankAccount("10003", "Jesse's Account", "Savings")


# Classes to represent employees in the banking app 
class Manager():
    def __init__(self, n, i, t): 
        self.name = n
        self.id = i 
        self.team = t 

    def display(self):
        print("Manager name is: " + self.name) 
        print("Manager id is: " + self.id)
        print("Manager team is " + self.team)

class Teller(): 
    def __init__(self, n, i, b): 
        self.name = name 
        self.id = i 
        self.branch = b 

    
    def display(self):
        print("Teller name is: " + self.name) 
        print("Teller id is: " + self.id)
        print("Teller branch " + self.branch)

# Now create objects of these classes 


# CLASS ATTRIBUTES VS INSTANCE ATTRIBUTES 
class Manager: 
    level = "L1" # this is a class attribute shared by all objects of this class 
    def __init__(self, firstname, lastname):
        self.firstname = firstname 
        self.lastname = lastname 

p2 = Manager("Jesse", "Mensah")
print(p2.level)


# Now using a class attribute in our account class 
class CheckingAccount: 
    type = "Checking" 
    def __init__(self, id, balance):
        self.account_id = id 
        self.balance = balance 

# Static Methods => all methods used so far can be executed when class has been instantiated 
# HOWEVERR WE CAN RUN A METHOD IN THE CLASS WITHOUT CREATING AN OBJECT 
class MathFormula: 
    def pow(self, x, y): 
        return x ** y 
m = MathFormula() 
print(m.pow(3, 3))


# static math formula 
class StatMathFormula: 
    @staticmethod 
    def pow(self, x, y): 
        return x ** y 

print(StatMathFormula.pow(3, 3))

# CLASS METHODS CAN BE CALLED WITHOUT INSTANTIATING THE CLASS 
class Sales: 
    sales_tax = 0.05 
    @classmethod 
    def applySalesTax(cls, amount): 
        return amount * (1+cls.sales_tax) 

    @classmethod 
    def applySalesTaxMany(cls, amounts): 
        out = list() 
        sales_tax = 0.06 
        out = [amount*(1+cls.sales_tax) for amount in amounts]
        return out 

print(Sales.applySalesTax(20))
print(Sales.applySalesTaxMany([10, 20, 30]))
    
# GOOGLE CLASS VS STATIC METHODS IN PYTHON 
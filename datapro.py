# PROCESSING TEXT FILES 

# SOME TERMS TO BE AWARE OF
# PATH -> IDENTIFIES THE LOCATION OF THE FILE TO BE UTILISED 
# ABSOLUTE PATH -> THIS INCLUDES ALL THE INFORMATION REQUIRED TO FIND THE FILE 
# RELATIVE PATH -> STARTS FROM THE DIRECTORY WHERE THE PYTHON SCRIPT IS STORED AND INCLUDES INSTRUCTIONS ON HOW TO GET THE FILE USING THAT 
# DIRECTORY AS A STARTING POINT. RELATIVE PATHS ARE SHORTER THAN ABSOLUTE PATHS 

# BASIC FUNCTIONS AND METHODS TO BE USED 
# INPUT , OPEN, READ, WRITE, CLOSE, PRINT 


f = open("GUT.txt", mode="r")
print(f.read(100)) 
f.close() 

# using the read mode to limit the content 
# print(f.read(100)) 

# creating functions that read characters from a file 
def head(filepath, num_char): 
    f = open(filepath, mode="r") 
    output = f.read(num_char)
    f.close() 
    return output 
text = head("GUT.txt", 20) 
print(text) 

# creating a function to readlines of a file 
def head(filepath, num_lines):
    f = open(filepath, mode="r") 
    # We create a variable called lines to hold the information we are reading from the file. 
    lines = "" 
    #  We then use a loop to iterate through reading the lines of the file using readline(). 
    for x in range(num_lines):
        lines += f.readline() 
    f.close() 
    return lines 

# ITERATING AND CHECKING THE START OF THE LINE 
def line_startswith(file_path, fchar):
    f = open(file_path, mode="r") 
    output= "" 
    for line in f: 
        if fchar == line[0]: 
            output += line 
    return output 
text = line_startswith("Alice.txt", "G")
print(text) 

# add content to a file 
f = open("Alice.txt", "a")
f.write('Jesse Mensah')


# writing a list to a file 
customers = ["Ax Lodevick", "Frank Prys", "Ania Hearle", "Justus Bodker", "Clementius Druce", "Ganny Penwright", "Alick Rens", "Gwen Drewitt", "Jessie Wychard",
"Brina Elliss", "Derril Damiral", "Jade Cutajar", "Brannon Goldsmith", "Valentin Salmons", "Tull Rennix", "Quintina Whanstall", "Lev Frunks", "Doris Heskin", "Idalina Moro", "Gillie Ledram"
]

def writelist2file(input_list, inputfilepath):
    f = open(inputfilepath, "a")
    for name in input_list: 
        name = "\n" + name 
        f.write(name) 
    f.close() 
writelist2file(customers, "GUT.txt")


# When checking something 
# Always think about membership -> if and else statements 


# READING CSV FILES 
import csv 

with open('stocks_short.csv') as f: 
    csv_file = csv.reader(f, delimeter=", ")
    row = f.readline() 
    print(row) 
    row = f.readline() 
    print(row) 

# ITERTAING THROUGH A CSV FILE 
with open('stocks_short.csv') as f: 
    csv_file = csv.reader(f, delimeter=', ')
    f.readline() 
    for row in csv_file:
        print(row) 
    
# iterate and print individual items 
with open('stocks_short.csv') as f: 
    csv_file = csv.reader(f, delimeter=', ')
    
    for row in csv_file:
        print(row[0], " - ", row[1]) 

# Creating a dictionary for each row in a csv file 
with open('stocks_short.csv') as f: 
    csv_file = csv.DictReader(f, delimeter=', ')
    
    for row in csv_file:
        print(row) 

# CREATING A LIST FROM THE DATASET 
def read_csv(filepath, delimeter=", "): 
    import csv 
    dataset = list() 
    with open(filepath) as f: 
        csv_file = csv.DictReader(f, delimeter=delimeter) 
        for row in csv_file:
            dataset.append(row) 
    return dataset 

dataset = read_csv("stocks_short.csv")
print(len(dataset)) 
print(dataset[0]) 
print(dataset) 


# USING LIST FROM READING CSV FILE TO CALCULATE THE CLOSING PRICE 
def read_csv(filepath, delimeter=", "): 
    import csv 
    dataset = list() 
    with open(filepath) as f: 
        csv_file = csv.DictReader(f, delimeter=delimeter) 
        for row in csv_file:
            dataset.append(row) 
    return dataset 
dataset = read_csv("stocks.csv") 
total = 0 
for row in dataset: 
    total += float[row["Close"]]
    print("Close: " + str[row["Close"]]) 
    print("------")
    print(total) 

# Writing data to a file row by row 
import csv
row_1 = ["employee_id","first_name","last_name"] # header row 
row_2 = ["EMP2345235636","robert","balti"] # first row
row_3 = ["EMP2498799899","mark","smith"] # second row
row_4 = ["EMP2498989890","mary","caldwell"] # third row
with open('data/employee.csv', 'w') as csv_file: # open file in write mode # use the writer class to create a writer object
# that we will use to write data into the file
    writer = csv.writer(csv_file,delimiter=',')
    writer.writerow(row_1) # writing the header row 
    writer.writerow(row_2) # writing the first row 
    writer.writerow(row_3) # writing the second row 
    writer.writerow(row_4) # writing the third row
f = open('data/employee.csv', 'r')
print(f.read())
f.close()

# PROMPTING THE USER FOR DATA FOR A CSV FILE 
import csv
with open('user_input.csv', 'w', newline='') as csv_file:
    while True:
      user_input = input("Please enter text to add to file [enter quit to exit]: ") 
      if user_input.lower() == 'quit':
          break 
      else:
          writer = csv.writer(csv_file,delimiter=',') 
          writer.writerow([user_input])
f = open('user_input.csv', 'r') 
print(f.read())
f.close()


# APPENDING DATA TO A CSV FILE 
import csv
row_1 = ["EMP4564576566","rodney","evans"] 
row_2 = ["EMP9807976875","lesa","clapper"] 
row_3 = ["EMP4564564566","mario","cruz"]
# first row # second row # third row
# open file in append mode, which will add
with open('data/employee.csv', 'a') as csv_file:
# use the writer class to create a writer object # that we will use to write data into the file 
       writer = csv.writer(csv_file,delimiter=',') 
       writer.writerow(row_1) # writing the first row 
       writer.writerow(row_2) # writing the second row 
       writer.writerow(row_3) # writing the third row
f = open('data/employee.csv', 'r') 
print(f.read())
f.close()

# WRITING MUTLIPLE FILES TO A ROW AT ONCE 
dataset = [["EMP9807976877","vicki","gallegos"],["EMP9807976872","hector","bowen"], ["EMP4564564598","cassandra","wang"]]



with open('data/employee.csv', 'a') as csv_file:
# use the writer class to create a writer object # that we will use to write data into the file 
    writer = csv.writer(csv_file,delimiter=',')
# write multiple rows at once using writerows 
    writer.writerows(dataset)
    f = open('data/employee.csv', 'r') 
    print(f.read())
    f.close()

# ADDING DICTIONARY OBJECTS TO A CSV FILE 
# create three rows of data; item order is not important because each dictionary # uses keys to identify each value
row_1 = {"employee_id":"EMP4564576566","first_name":"rodney","last_name":"evans"} 
row_2 = {"first_name":"lesa","last_name":"clapper","employee_id":"EMP9807976875"} 
row_3 = {"employee_id":"EMP4564564566","last_name":"cruz","first_name":"mario"}

fieldnames = ["employee_id","first_name","last_name"]
with open('data/employee.csv', 'w') as csv_file:
     writer = csv.DictWriter(csv_file,delimiter=',',fieldnames=fieldnames) 
     writer.writeheader()
     writer.writerow(row_1) # write the first row
     writer.writerow(row_2) # write the second row
     writer.writerow(row_3) # writethe third row
f = open('data/employee.csv', 'r') 
print(f.read())
f.close()

# ADDING TRANSACTIONS VIA DICTIONARIES 
import csv,os
count = 0 
filename='transactions.csv' 
dataset = {}

trans_date = input("Please enter the transaction date: ") 
customer = input("Enter the customer: ")
merchant = input("Enter the merchant name: ")
total = input("Enter the total of the transaction: ")

input_data = {"trans_date":trans_date,"customer":customer, "merchant":merchant,"total":total}
print(input_data)

fieldnames = ["trans_date","customer","merchant","total"]

# Open file in append mode, which will add the data at the # end of the file
if os.path.exists(filename):
    with open(filename, 'a') as csv_file:
       writer = csv.DictWriter(csv_file,fieldnames=fieldnames) 
       writer.writerow(input_data)
else:
    with open(filename, 'w') as csv_file:
      writer = csv.DictWriter(csv_file,fieldnames=fieldnames) 
      writer.writeheader()
      writer.writerow(input_data)

# print out the data in the file 
f = open('transactions.csv', 'r')
print(f.read()) 
f.close() 

# PROCESSING JSON FILES -> NOT NECESSAY ATM 
#to Read the CSV
""" import csv
with open('filename.csv', 'operation') as file:
    reader = csv.reader(file)
    
    for  row in reader:
        print(row)
"""      

import csv 

with open('sales.csv','r') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        print(row)
        
        
#to Remove Bad Records

        cleaned_data = []

with open("sales.csv", "r") as file:               #to open file 
    reader = csv.DictReader(file)                  #to read the file as dictionary

    for row in reader:                            #to iterate through each row
        if row["customer"] and row["amount"] and row["city"]:     #to check if the values are not empty
            cleaned_data.append(row)

with open("cleaned_sales.csv", "w", newline="") as file:   #to open file to write the cleaned data
    writer = csv.DictWriter(                               #to write the cleaned data to a new CSV
        file,
        fieldnames=["order_id", "customer", "product", "amount", "city"]   #to specify the fieldnames for the new CSV
    )

    writer.writeheader()                        #write the header row to the new CSV
    writer.writerows(cleaned_data)              #write the cleaned data to the new CSV

print("Data Cleaning Complete!")                #to print a message indicating that the data cleaning process is complete
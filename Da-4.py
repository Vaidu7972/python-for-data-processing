#to Calculate total sales amount

import csv
   
total_sales = 0    # to initialize a variable to store the total sales amount


with open("sales.csv", "r") as file:     #to open the CSV file in read mode
    reader = csv.DictReader(file)

    for row in reader:
        if row["amount"]:  # Ignore missing amounts
            total_sales += int(row["amount"])

print("Total Sales Amount:", total_sales)  # to print the total sales amount


highest_sales = 0

with open('sales.csv','r') as file : 
    reader =  csv.DictReader(file)
    for row in reader:
        if row["amount"] and int(row["amount"]) > highest_sales:
            amount = int(row["amount"])
            
            if amount > highest_sales:
                highest_sales = amount

print("Highest Sales Amount:", highest_sales)  # to print the highest sales amount  
            
lowest_sales = float('inf')  # Initialize to infinity for comparison

with open('sales.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["amount"] and int(row["amount"]) < lowest_sales:
            amount = int(row["amount"])
            
            if amount < lowest_sales:
                lowest_sales = amount
            
print("Lowest Sales Amount:", lowest_sales)  # to print the lowest sales amount 

# to Calculate sales by city using a dictionary

sales_by_city = {}  # to create an empty dictionary to store sales by city      

with open("sales.csv", "r") as file:  # to open the CSV file in read mode
    reader = csv.DictReader(file)

    for row in reader:
        city = row["city"]
        amount = int(row["amount"]) if row["amount"] else 0  # Handle missing amounts

        if city in sales_by_city:
            sales_by_city[city] += amount
        else:
            sales_by_city[city] = amount

print(sales_by_city)  # to print the sales by city dictionary

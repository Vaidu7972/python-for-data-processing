
#In this we use csv module to read and write CSV files, 
# and we clean the data by removing any rows that have empty values in the "customer", "amount", or "city" columns. 
# The cleaned data is then written to a new CSV file called "cleaned_sales.csv".

import csv    #to import the csv module for reading and writing CSV files

cleaned_data = []   #to create an empty list to store the cleaned data

with open('sales.csv','r') as file:  #to open  file and reading it
    reader = csv.DictReader(file)   #to read file as dictionary 
    
    for row in reader:  #to iterate through each row in CSV file
        if row["customer"] and row["amount"] and row["city"]:#to check if the values are not empty
            cleaned_data.append(row)  #to append the cleaned data to the list'
            

with open('cleaned_sales.csv','w',newline='') as file: #to open file to write cleaned data  
    writer = csv.DictWriter(
        file, #to write the cleaned data to a new CSV file
        fieldnames=["order_id", "customer", "product", "amount", "city"]  #to specify the fieldnames for the new CSV    

    )   
    
    writer.writeheader() #to write the header row to the new CSV file
    writer.writerows(cleaned_data) #to write the cleaned data to the new CSV file   
print("Data Cleaning Complete!") #to print a message indicating that the data cleaning process is complete  
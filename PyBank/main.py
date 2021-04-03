import os
import csv
import statistics

# Set path for reading a file
csv_bank = os.path.join("PyBank","Resources","bank.csv")

# Open the CSV
with open(csv_bank, newline='') as csvfile:
 
 # CSV reader specifies delimiter and variables that holds content
    csv_reader = csv.reader(csvfile, delimiter=",")
    
# Read the Heeader row first  (skip this step if there is no header)
    header = next(csv_reader)
    
    print(f'CSV Header: {header}')
    
    
# Calculate the total number of months included in the dataset
    
    total_months=0
    for row in csv_reader:
        if row[0] != 0:
            total_months = sum(1 for row in csv_reader)
        else:
            total_months=total_months
    print(total_months)  # Wrong the result should be 86

    
# The net total amount of "Profit/Losses" over the entire period
    net_profit=0
    
    for row in csv_reader:
        
        net_profit= (int(row[1]+1) + int(row[1])
                     
    print(f' Net Total amount of Profit/Losses is: {net_profit}')
        
        
# Calculate the changes in "Profit/Losses" over the entire period, then 
# find the average of those changes

    changes_profit=0

    for row in csv_reader:
        
        changes_profit= (int(row[1]+1) + int(row[1])
    
# The greatest increase in profits (date and amount) over the entire period

    for row in csv_reader:
        increase= (int(row[1]+1) - int(row[1])
        
        great_increase=0
        
        if increase > great_increase:
            great_increase = great_increase + increase
        print(f'{greatest_increase}, {row[0]}')
        print(f'{greatest_increase}, {row[1]}')

# The greatest decrease in losses (date and amount) over the entire period
# for row in csv_reader:
        decrease= (int(row[1]+1) - int(row[1])
        
        great_increase=min(decrease)
        
        if decrease < great_decrease:
            great_increase = great_increase + decrease
        print(f'{greatest_increase}, {row[0]}')
        print(f'{greatest_increase}, {row[1]}')
# 
# 
# The net total amount of "Profit/Losses" over the entire period
    
    
    
    
 # Print statements 
 
 
 # Creating a file
  # 1. Specify the file to write to
output_path = os.path.join("PyBank","Resources","bank_solution.csv")
 
 # 2. Open a file using "write mode" specify the variable that holds the content
 with open(output_path, "w" ,newline='') as csvfile:
 
 # 3. Initialize csv.writer
 csv_writer= csv.writer(csvfile, delimiter=',')

 # 4. Write the first row (columns, headers)
csvwriter.writerow("Financial Analysis ")

csvwriter.writerow(f'Total Months: {total_monmths}')
csvwriter.writerow(f'Total Months: {net_profit}')
csvwriter.writerow(f'Total Months: {changes_profit}')
  csvwriter.writerow(f'Total Months: {total_monmths}') 
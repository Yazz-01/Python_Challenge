import os
import csv
import statistics

# Set path for reading a file
csv_bank = os.path.join(".","Resources","bank.csv")

# Open the CSV
with open(csv_bank, newline='') as csvfile:
 
 # CSV reader specifies delimiter and variables that holds content
    csv_reader = csv.reader(csvfile, delimiter=",")
    
# Read the Heeader row first  (skip this step if there is no header)
    header = next(csv_reader)
    
    print(f'CSV Header: {header}')
    
# Calculate the total number of months included in the dataset
    
    total_months=0
    net_profit=0
    changes_profit=0
    total_changes_profit=0
    count = 0
    changes = []
    average_change=0
    great_increase_prof=0
    great_decrease_prof=0

# Looping through the document
    for row in csv_reader:
       
# Total number of months of the entire period      
        total_months=total_months + 1
    
# The net total amount of "Profit/Losses" over the entire period
    
        net_profit = net_profit + int(row[1])
        
# Calculate the changes in "Profit/Losses" over the entire period

        if count==0:
            changes_profit=0
            current= int(row[1])
            count=count+1
        else:
            changes_profit= int(row[1])-current
            changes.append(changes_profit)
            current= int(row[1])
            
# The Average change over the period
            average_change= round(sum(changes)/len(changes),2)
            
# The greatest increase in profits (date and amount) over the entire period
            
            if changes_profit > great_increase_prof:
                great_increase_prof=changes_profit
                great_increase_date= row[0]
                
# The greatest decrease in losses (date and amount) over the entire period 
            if  changes_profit < great_decrease_prof :
                great_decrease_prof =changes_profit
                great_decrease_date= row[0]
                
output_path=os.path.join("Output", "new.txt")   
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:

# #     # Initialize csv.writer
     #csvwriter = csv.writer(csvfile, delimiter=',')

# #     # Write the first row (column headers)
    txtfile.write(f'\n')
    txtfile.write(f'Financial Analysis\n')
    txtfile.write(f'---------------------------\n')
    txtfile.write(f'Total Months: {total_months}\n')
    txtfile.write(f'Total: ${net_profit}\n')
    txtfile.write(f'Average Change: ${changes_profit}\n')
    txtfile.write(f'Greatest Increase in Profits: {great_increase_date} (${great_increase_prof})\n')
    txtfile.write(f'Greatest Decrease in Profits: {great_decrease_date} (${great_decrease_prof})\n')
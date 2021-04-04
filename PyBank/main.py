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
    net_profit=0
    changes_profit=0
    total_changes_profit=0
    count = 0
    changes = []
    average_change=0
    great_increase_prof=0
    
    great_decrease_prof=0
    for row in csv_reader:
        #print(row[1])
        total_months=total_months + 1
    
# The net total amount of "Profit/Losses" over the entire period
    
        net_profit = net_profit + int(row[1])
        
# Calculate the changes in "Profit/Losses" over the entire period, then 
# # find the average of those changes
        date_changes= row[0]
        if count==0:
            changes_profit=0
            current= int(row[1])
            count=count+1
        else:
            changes_profit= int(row[1])-current
            changes.append(changes_profit)
            current= int(row[1])
            #changes=[date_changes,int(changes_profit)]
# The Average change
            average_change= sum(changes)/len(changes)
# The greatest increase in profits (date and amount) over the entire period
            great_increase_prof= max(changes)
            #great_increase_date= great_increase_prof.index(0)
# The greatest decrease in losses (date and amount) over the entire period 
            great_decrease_prof= min(changes)
            #great_decrease_date= great_decrease_prof.index(0)
                     
    
    print(f'Total Months: {total_months}') 
    print(f"Total: {net_profit} ")
    print(f"Average  Change: {average_change} ")
    print(f'Greatest Increase in Profits: (${great_increase_prof})') 
    print(f'Greatest Decrease in Profits: (${great_decrease_prof})') 
  
 
# Save the output file path
output_file=os.path.join("output.csv")
# Initialize csv.writer
csvwriter=csv.writer(csvfile,delimiter=',')
#Write th first row (column headers)
# csvwriter.writerow([Total Months: {total_monmths}])
# csvwriter.writerow([Total Months: {net_profit}])
# csvwriter.writerow([Total Months: {changes_profit}])
# csvwriter.writerow([Total Months: {total_monmths}}) 
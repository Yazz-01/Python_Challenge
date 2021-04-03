import os
import csv
import statistics

# Set path for reading a file
csv_poll = os.path.join("PyPoll","Resources","election_data.csv")

# Open the CSV
with open(csv_poll, newline='') as csvfile:
 
 # CSV reader specifies delimiter and variables that holds content
    csv_reader = csv.reader(csvfile, delimiter=",")
    
# Read the Heeader row first  (skip this step if there is no header)
    header = next(csv_reader)
    
    print(f'CSV Header: {header}')
    
    
# Calculate the total number of months included in the dataset
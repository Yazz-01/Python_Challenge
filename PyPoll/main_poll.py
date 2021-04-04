import os
import csv
import statistics

# Set path for reading a file
csv_poll = os.path.join("PyPoll","Resources","election_data.csv")

# Open the CSV
with open(csv_poll, newline='') as csvfile:
 
 # CSV reader specifies delimiter and variables that holds content
    file_csv = csv.reader(csvfile, delimiter=",")
    print(file_csv)
# Read the Heeader row first  (skip this step if there is no header)
    header = next(file_csv)
    print(f'CSV Header: {header}')
    
    
# The total number of votes cast
total_votes=0
for row in file_csv:
    total_votes =int(row[0])+ int(row[0])+1
    print(row)

# A complete list of candidates who received votes


# The percentage of votes each candidate won


# The total number of votes each candidate won


# The winner of the election based on popular vote.
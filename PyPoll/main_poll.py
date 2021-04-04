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
    count=0
    total_votes=0
    lst_candidates={}
    
    for row in file_csv:
        total_votes = total_votes+ int(row[0])
        
        lst_candidates.append(row[2])
# A complete list of candidates who received votes
        #count=sum(int(row[2]))
        
        #lst_candidates.append.(int(row[])row[2])

# The percentage of votes each candidate won


# The total number of votes each candidate won


# The winner of the election based on popular vote.

    
    print(f'Total Votes {total_votes}')
    print(f'{lst_candidates}')

import os
import csv
import statistics
from decimal import getcontext, Decimal
import operator


# Set path for reading a file
csv_poll = os.path.join("PyPoll","Resources","election_data.csv")

# Open the CSV
with open(csv_poll, 'r') as csvfile:

# CSV reader specifies delimiter and variables that holds content
    csv_poll = csv.reader(csvfile, delimiter=",")
    
# Read the Heeader row first  (skip this step if there is no header)
    header = next(csv_poll)
    print(f'CSV Header: {header}') 
    

# Variables
    
    total_votes=0
    candidates=set()
    cand_votes_counts={}
    perctg_votes=[]
# Looping through the file    
    for row in csv_poll:
        vote= int(row[0])
        candidate= row[2]
        
# The total number of votes of candidates         
        total_votes=total_votes+ 1
        
# A complete list of candidates who received votes 
        candidates.add(candidate)  
             
# The total number of votes per candidate      
 
        cand_votes_counts[candidate]=cand_votes_counts.get(candidate,0)+ 1
        
# The percentage of votes each candidate won 
# Set precision
        
        perctg_votes=[(k,round(v/total_votes*100,4)) for k,v in cand_votes_counts.items()]
        
# Get the winner from the election
        winner= max(cand_votes_counts, key=cand_votes_counts.get)
        
    print(f'{total_votes} ')     
    print(f'{candidates}')
    print(f'{cand_votes_counts}')
    print(f'{perctg_votes}')
    print(f'{winner}')



# # Open the file using "write" mode. Specify the variable to hold the contents
    output_file = open(os.path.join("Election Analysis","pypoll_election","new.csv", 'w', newline='') as csvfile:

#     # Initialize csv.writer
    
#     # Write the first row (column headers)
    output_file.write(['Election Results'])
    output_file.write(['-----------------------'])
#     # Write the second row
    output_file.write(['Total Votes: {total_votes}'])
    output_file.write(['Total Votes: {candidates}'])
    output_file.write(['Total Votes per candidate: %{cand_votes_counts}'])
    output_file.write(['Winner: {winner}'])
    
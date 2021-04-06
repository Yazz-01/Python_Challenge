import os
import csv
import statistics

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

    candidates = set()
    total_votes=0
    cand_votes_counts=[]
# Looping through the file    
    for row in csv_poll:
        candidate= row[2]
        vote= int(row[0])
        found= False
# The total number of votes of candidates  
        total_votes=total_votes+vote
        
# A complete list of candidates who received votes 
        candidates.add(candidate)       

# The percentage of votes each candidate won
        for entry in cand_votes_counts:
            if entry[0]==candidate:
                entry[1]=entry[1]+1
                found=True
                
        if not found:
           cand_votes_counts.append([candidate,1])  

    
    #total_votes=[vote for vote in num_votes]
    
    #print(f'{total_votes}')

    print(f'{candidates}')
    print(f'{total_votes}')
    print(f'{cand_votes_counts}')
        



#percent_votes= round(int(row[])/int(row[]),2)


# The total number of votes each candidate won


# The winner of the election based on popular vote.

    
    



# # Specify the file to write to
# output_path = os.path.join("..", "output", "new.csv")

# # Open the file using "write" mode. Specify the variable to hold the contents
# with open(output_path, 'w', newline='') as csvfile:

#     # Initialize csv.writer
#     csvwriter = csv.writer(csvfile, delimiter=',')

#     # Write the first row (column headers)
#     csvwriter.writerow(['First Name', 'Last Name', 'SSN'])

#     # Write the second row
#     csvwriter.writerow(['Caleb', 'Frost', '505-80-2901'])

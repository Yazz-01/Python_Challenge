import os
import csv
import statistics

# Set path for reading a file
csv_poll = os.path.join("PyPoll","Resources","election_data.csv")

# Open the CSV
with open(csv_poll, 'r') as text:
    print(text)
    
# Store all of the text inside a variable called "lines"
    lines = text.read()
    
# Variables
    votes_count=[]
    candidates_count=[]
    votes_candidates={}
    total_votes=0
# Looping through the file
    for row in lines:
        
        votes_count.append(row[0])  
        candidates_count.append(row[2]
        votes_candidates = candidates_count                     
        #votes_candidates[canditates_count]=votes_count
        
        print(f'{votes_candidates}')
        
        #print(f'Total Votes {total_votes}')
        #print(f'{lst_candidates}')
        #total_votes = total_votes+ int(row)+1
        
        #lst_candidates= 
        
# The total number of votes cast

# A complete list of candidates who received votes
        #count=sum(int(row[2]))
        
        #lst_candidates.append.(int(row[])row[2])

# The percentage of votes each candidate won


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

In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.

You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:


The total number of votes cast


A complete list of candidates who received votes


The percentage of votes each candidate won


The total number of votes each candidate won


The winner of the election based on popular vote.

Run the loop:
    every time a new name occurs(condition):
        append that name to the dictionary with 0 votes a[name] = 0
    a[name] add by 1 vote
    
    
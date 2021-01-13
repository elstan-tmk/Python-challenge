import os 

import csv

# electioncsv = os.path.join('/Users/mic_elstan/Desktop/UC Davis Bootcamp/Homeworks/Python-Challenge/Python-challenge/PyPoll/Resources/election_data.csv')

with open("Resources/election_data.csv", 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')

    header = next(csvreader)
    vote_cast = 0
    candidates = []
    khan_vote = 0
    correy_vote = 0
    li_vote = 0
    toolet_vote = 0

    for vote in csvreader:

        # vote[2] bc the candidate name is on the 3rd column
        vote_cast += 1   

        if(vote[2] == "Khan"):
            khan_vote += 1
        elif(vote[2] == " Correy"):
            correy_vote += 1
        elif(vote[2] == "Li"):
            li_vote += 1
        else:
            toolet_vote += 1

    khan_percent = (khan_vote / vote_cast) *100
    correy_percent = (correy_vote / vote_cast) *100
    li_percent = (li_vote / vote_cast) *100
    toolet_percent = (toolet_vote / vote_cast) *100

    list_of_candidate = ["Khan", "Correy", "Li", "O'Tooley"]
    vote = [khan_vote, correy_vote, li_vote, toolet_vote]
            
    vote_cast_dict = dict(zip(list_of_candidate, vote))
    key = max(vote_cast_dict, key = vote_cast_dict.get)

print(f"Election Results")
print(f"--------------------------------------")
print(f"Total Votes: {vote_cast}")
print(f"--------------------------------------")
print(f"Khan:  {khan_percent:.3f} % {khan_vote} ")            
print(f"Correy: {correy_percent:.3f} % {correy_vote}")
print(f"Li: {li_percent:.3f} % {li_vote}")
print(f"O'Tooley: {toolet_percent:.3f} % {toolet_vote}")
print(f"--------------------------------------")
print(f"Winner: {key}")
print(f"=======================================")


data_output = os.path.join("poll_data.txt")

with open(data_output, 'w') as csvfile:                       
    csvfile.write("Election Results\n")
    csvfile.write(f"--------------------------------------\n")
    csvfile.write(f"Total Votes: {vote_cast}\n")
    csvfile.write(f"--------------------------------------\n")
    csvfile.write(f"Khan:  {khan_percent:.3f} % {khan_vote} \n")              
    csvfile.write(f"Correy: {correy_percent:.3f} % {correy_vote}\n")
    csvfile.write(f"Li: {li_percent:.3f} % {li_vote}\n")
    csvfile.write(f"O'Tooley: {toolet_percent:.3f} % {toolet_vote}\n")
    csvfile.write(f"--------------------------------------\n")
    csvfile.write(f"Winner: {key}\n")
    csvfile.write(f"=======================================\n")


    
import os 

import csv

electioncsv = os.path.join('/Users/mic_elstan/Desktop/UC Davis Bootcamp/Homeworks/Python-Challenge/Python-challenge/PyPoll/Resources/election_data.csv')

with open(electioncsv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')

    header = next(csvreader)
    vote_cast = 0
    candidates = []
    khan_vote = 0
    correy_vote = 0
    li_vote = 0
    toolet_vote = 0

    for vote in csvreader:
        vote_cast += 1

        # vote[2] bc the candidate name is on the 3rd column
        candidates.add (vote[2])    # <------- not working Carmen, my code is not working, can you please help checking?

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
            
    vote_cast_dict = dict(list_of_candidate, vote)
    winner = max(vote_cast_dict, winner=vote_cast_dict.get)

    print("Election Results")
    print("--------------------------------------")
    print("Total Votes: " + str(vote_cast))
    print("--------------------------------------")
    print("Khan: " + (khan_percent) + "% " + (str(khan_vote)))              # <------- how to make them .000%??
    print("Correy: " + (correy_percent)) + "% " + (str(correy_vote)))
    print("Li: " + (li_percent) + "% " + (str(li_vote)))
    print("O'Tooley: " + (toolet_percent) + " " + (str(toolet_vote)))
    print("---------------------------------------")
    print("Winner: " + winner)
    print("=======================================")


    ouput_file = '/Users/mic_elstan/Desktop/UC Davis Bootcamp/Homeworks/Python-Challenge/Python-challenge/Export.txt'

    with open(ouput_file, 'w') as file:                        # <---------- do we need to create a file before file.write? or will it create a new file on its own
    file.write("Election Results")
    file.write("--------------------------------------")
    file.write("Total Votes: " + str(vote_cast))
    file.write("--------------------------------------")
    file.write("Khan: " + (khan_percent) + "% " + (str(khan_vote)))             
    file.write("Correy: " + (correy_percent)) + "% " + (str(correy_vote)))
    file.write("Li: " + (li_percent) + "% " + (str(li_vote)))
    file.write("O'Tooley: " + (toolet_percent) + " " + (str(toolet_vote)))
    file.write("---------------------------------------")
    file.write("Winner: " + winner)
    file.write("=======================================")


    
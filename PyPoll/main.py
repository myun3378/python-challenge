import os
import csv

csv_path = ["election_data_2.csv","election_data_1.csv"]
output_path = 'election_results.csv'

candidates = []
total_votes = 0
candidates_vote = 0
percent_vote = 0
winner_count = 0

for datafiles in csv_path:
    with open (datafiles, newline="") as csvfile:
        csvreader = csv.reader (csvfile, delimiter=",")

        next (csvreader,None)
        
        for row in csvreader:
            total_votes = total_votes + 1
            candidates.append (row[2])
    
candidates_set = set (candidates)

paper_results = open (output_path,"w",newline="")
print (" "*30)
print ("Total Votes: " + str(total_votes))
print ("-"*30)
paper_results.write ("Total Votes: "+ str(total_votes))
paper_results.write ("\n-------------------------\n")

for names in candidates_set:
    candidates_vote = candidates.count (names)
    if candidates_vote > winner_count:
        winner_name = names
        winner_count = candidates_vote
    percent_vote = round(((candidates_vote / total_votes)*100),2)
    print (names + ": " + str(percent_vote)+"%   ("+ str(candidates_vote)+")")
    paper_results.write (names + ": " + str(percent_vote)+"%   ("+ str(candidates_vote)+")\n")
    candidates_vote = 0

print ("-"*30)
print ("Winner: " + winner_name)
print ("-"*30)

paper_results.write ("-------------------------\n")
paper_results.write ("Winner: " + winner_name)
paper_results.write ("\n---------------------------")


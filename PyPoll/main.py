import os
import csv
import sys

# Path to collect data from the Resources folder
csvpath = os.path.join('Resources', 'election_data.csv')

votes = []
candidates = []
poll = {}
votepercentage = []

# Read in the CSV file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # Loop through the data
    for row in csvreader:
        votes.append(int(row[0]))
        candidates.append(str(row[2]))  
        totalvotes = len(votes)
        if row[2] in poll.keys():
         poll[row[2]]=poll[row[2]]+1
        else:
            poll[row[2]] = 1
highestvote = max(poll, key=poll.get)
#print(poll.keys())
#Print outs
sys.stdout = open("electionresults.txt", "a")
print("Election Results")
print("-"*25)
print("Total Votes:", totalvotes)
print("-"*25)
for k,v in poll.items():
    percent = round(float((v/totalvotes)*100), 2)
    print(k, percent,"%", v,"votes")
print("-"*25)
print("Winner:", highestvote, "with", poll[highestvote], "votes")
print("-"*25)

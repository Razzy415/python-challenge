import os
import csv
import sys

# Path to collect data from the Resources folder
csvpath = os.path.join('Resources', 'election_data.csv')


# My super awesome function for calculating poll data
#def getPercentages(polldata):

    # Total votes
    #totalvotes = len(int(polldata[0])) 

    # Vote percentage
    #votepercentage = (int(polldata[0]) / totalvotes) * 100

    # Print out the wrestler's name and their percentage stats
    #print("Election Results")
    #print("-------------------------")
    #print("Total Votes:", sum(votes))
    #print("-------------------------")
   

votes = []
candidates = []
uniquecandidates = []
poll = {}

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
#Print outs
sys.stdout = open("electionresults.txt", "w")
print("Election Results")
print("-"*25)
print("Total Votes:", totalvotes)
print("-"*25)
for k,v in poll.items():
    print(k, v)
print("-"*25)
print("Winner:", highestvote, "with", poll[highestvote], "votes")
print("-"*25)

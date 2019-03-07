import os
import csv
import sys

# File path
csvpath = os.path.join("Resources", "budget_data.csv")

# List storage
PL = []
date = []
PLdelta = []

# Read in file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    #iterate through rows and store in list
    for row in csvreader:
        PL.append(float(row[1]))
        date.append(row[0])
        #iterate through the P/L and obtain min and max, while getting delta
        for i in range(1, len(PL)-1):
            PLdelta.append(PL[i+1] - PL[i])   
            avg_PLdelta = sum(PLdelta)/len(PLdelta)
            maxPL = max(PL)
            minPL = min(PL)
            maxPLdate = str(date[PL.index(max(PL))])
            minPLdate = str(date[PL.index(min(PL))])
#Print outs
sys.stdout = open("financialanalysis.txt", "w")
print("Financial Analysis", )
print("-----------------------------------")
print("Total months:", len(date))
print("Total: $", sum(PL))
print("Average change in profit/loss: $", round(avg_PLdelta))
print("Greatest Increase in Profits:", maxPLdate,"($", maxPL,")")
print("Greatest Decrease in Profits:", minPLdate,"($", minPL,")")

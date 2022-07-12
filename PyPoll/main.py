import os
import csv
import numpy as np

election_csv = os.path.join("Resources", "election_data.csv" )
BallotIDCount = []
County = []
Candidates = set()
AllCandidates= []
CandidateCountDict = {}


with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    next(csvreader)
    for row in csvreader:
        BallotIDCount.append(row[0])
        County.append(row[1])
        Candidates.add(row[2])
        AllCandidates.append(row[2])

    CandidateCountDict = {item:AllCandidates.count(item) for item in Candidates}
Charles = CandidateCountDict["Charles Casper Stockham"]
Raymon = CandidateCountDict["Raymon Anthony Doane"]
Diana = CandidateCountDict["Diana DeGette"]

s = sum(CandidateCountDict.values())
for k, v in CandidateCountDict.items():
    percent = v *100.0 / s

    

print(len(BallotIDCount))
print(CandidateCountDict)
print(k,percent)
print(k,percent)
print(k,percent)


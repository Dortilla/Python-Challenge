import os
import csv

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
charlespercent = round(Charles *100.0 / s , 3)
raymonpercent = round(Raymon *100.0 / s, 3)
dianapercent = round(Diana *100.0 / s, 3)
winner = max(CandidateCountDict, key=CandidateCountDict.get)
totalvotes= len(BallotIDCount)

toprint = f"""Election Results
--------------------------------------
Total Votes:  {totalvotes}
--------------------------------------
Charles Casper Stockham:
{charlespercent}% ( {Charles} )
Diana Degette:
{dianapercent}% ( {Diana} )
Raymon Anthony Doane:
{raymonpercent}% (  {Raymon} )
--------------------------------------
Winner: {winner}
--------------------------------------"""

print(toprint)

analysispath = os.path.join("Analysis" , 'results.txt')
with open(analysispath, "w") as analysisresults:
    analysisresults.writelines(toprint)
analysisresults.close()

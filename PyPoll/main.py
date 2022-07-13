import os # importing modules that i will be working with throughout this assignment
import csv

election_csv = os.path.join("Resources", "election_data.csv" ) # designate location of files that i will be using  
analysispath = os.path.join("Analysis" , 'results.txt')

BallotIDCount = [] # designate variables
County = []
Candidates = set()
AllCandidates= []
CandidateCountDict = {}


with open(election_csv) as csvfile: # opening the csv file
    csvreader = csv.reader(csvfile, delimiter= ",")
    next(csvreader) # skipping header row 
    for row in csvreader:
        BallotIDCount.append(row[0]) #updating variables to have values
        County.append(row[1])
        Candidates.add(row[2])
        AllCandidates.append(row[2])

    CandidateCountDict = {item:AllCandidates.count(item) for item in Candidates} #creating dictionary containing each candidate and how many votes they recieved
Charles = CandidateCountDict["Charles Casper Stockham"]
Raymon = CandidateCountDict["Raymon Anthony Doane"]
Diana = CandidateCountDict["Diana DeGette"]

s = sum(CandidateCountDict.values()) # calculating percentage of votes for each candidate, as well as  the winner
charlespercent = round(Charles *100.0 / s , 3)
raymonpercent = round(Raymon *100.0 / s, 3)
dianapercent = round(Diana *100.0 / s, 3)
winner = max(CandidateCountDict, key=CandidateCountDict.get)
totalvotes= len(BallotIDCount)

#saving the results of analysis 
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

print(toprint) #print results to terminal 


with open(analysispath, "w") as analysisresults: # create and open file for analysis results
    analysisresults.writelines(toprint) # write the data of "Election Results" to results.txt
analysisresults.close() # close results.txt

import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv" )

date = []
revenue = [] 
revenue_change = []
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        date.append(row[0])
        revenue.append(float(row[1]))



    for i in range(1,len(revenue)):
        revenue_change.append(revenue[i] - revenue[i-1])
    
        avg_revenue_change = sum(revenue_change) / len(revenue_change)
    
        max_revenue_change = max(revenue_change)
    
        min_revenue_change = min(revenue_change)
    
        max_revenue_change_date = str(date[revenue_change.index(max(revenue_change))])
        min_revenue_change_date = str(date[revenue_change.index(min(revenue_change))])



print("Financial Analysis")
print("------------------")
print("Total Months: ", len(date))
print("Total: ", sum(revenue))
print("Average Change: " , avg_revenue_change)
print("Greatest Increase in Profits: " , max_revenue_change_date, "(" , max_revenue_change , ")")
print("Greatest Decrease in Profits: " , min_revenue_change_date , "(" , min_revenue_change , ")")

resultspath = os.path.join("Analysis" , "results.txt" )
with open(resultspath , "w") as external_file: 
    print("Financial Analysis" , file=external_file)
    print("------------------", file=external_file)
    print("Total Months: ", len(date), file=external_file)
    print("Total: ", sum(revenue), file=external_file)
    print("Average Change: " , avg_revenue_change, file=external_file)
    print("Greatest Increase in Profits: " , max_revenue_change_date, "(" , max_revenue_change , ")", file=external_file)
    print("Greatest Decrease in Profits: " , min_revenue_change_date , "(" , min_revenue_change , ")", file=external_file)
external_file.close()
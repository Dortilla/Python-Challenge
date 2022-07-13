import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv" ) # assign path of file to 'budget_csv'

date = [] #variables 
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

        rounded_average_revenue = round(avg_revenue_change , 2)
        max_revenue_change = max(revenue_change)
    
        min_revenue_change = min(revenue_change)
    
        max_revenue_change_date = str(date[revenue_change.index(max(revenue_change))])
        min_revenue_change_date = str(date[revenue_change.index(min(revenue_change))])

toprint = f"""Financial Analysis
------------------
Total Months:  {len(date)}
Total: ${round(sum(revenue))}
Average Change: ${round(avg_revenue_change, 2)}
Greatest Increase in Profits: {max_revenue_change_date} (${max_revenue_change}) 
Greatest Decrease in Profits: {min_revenue_change_date} (${min_revenue_change}) """
print(toprint)

resultspath = os.path.join("Analysis" , "results.txt" )
with open(resultspath , "w") as external_file: 
 external_file.writelines(toprint)
external_file.close()
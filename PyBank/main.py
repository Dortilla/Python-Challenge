import os # importing modules that I will be using in this assignment
import csv

budget_csv = os.path.join("Resources", "budget_data.csv" ) # assign paths to files i will be using
resultspath = os.path.join("Analysis" , "results.txt" )

date = [] # designating variables 
revenue = [] 
revenue_change = []

with open(budget_csv) as csvfile: # opening csv file
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader) # skipping header
    for row in csvreader:
        date.append(row[0]) # updating variables
        revenue.append(float(row[1]))



    for i in range(1,len(revenue)): # calculate avg revenue change, along with finding days of min and max revenue change
        revenue_change.append(revenue[i] - revenue[i-1]) 
    
        avg_revenue_change = sum(revenue_change) / len(revenue_change)

        rounded_average_revenue = round(avg_revenue_change , 2)
        max_revenue_change = max(revenue_change)
    
        min_revenue_change = min(revenue_change)
    
        max_revenue_change_date = str(date[revenue_change.index(max(revenue_change))])
        min_revenue_change_date = str(date[revenue_change.index(min(revenue_change))])

# saving analysis results
toprint = f"""Financial Analysis 
------------------
Total Months:  {len(date)}
Total: ${round(sum(revenue))}
Average Change: ${round(avg_revenue_change, 2)}
Greatest Increase in Profits: {max_revenue_change_date} (${max_revenue_change}) 
Greatest Decrease in Profits: {min_revenue_change_date} (${min_revenue_change}) """
print(toprint)

with open(resultspath , "w") as external_file: # create / open results.txt
 external_file.writelines(toprint) # write contents of 'toprint' in results.txt
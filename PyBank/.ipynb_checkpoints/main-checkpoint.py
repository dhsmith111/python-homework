# Instructions: https://rice.bootcampcontent.com/Rice-Coding-Bootcamp/ru-hou-fin-pt-06-2020-u-c/tree/master/Homework/02-Python/Instructions

# Your task is to create a Python script that analyzes the records to calculate each of the following:
#  The total number of months included in the dataset.
#  The net total amount of Profit/Losses over the entire period.
#  The average of the changes in Profit/Losses over the entire period.
#  The greatest increase in profits (date and amount) over the entire period.
#  The greatest decrease in losses (date and amount) over the entire period.
#
#
#Your resulting analysis should look similar to the following:
#
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)
#
# Your final script should print the analysis to the terminal and export a text file with the results.
#
#

# import libraries
from pathlib import Path
import csv

# set the csv file name and path
csv_pathfile = './PyBank_Resources_budget_data.csv'

# initialize list for budget data,
budget_data = []
    
# Open file to read records
with open (csv_pathfile, 'r') as csv_file:

    #use csv.reader to collect file object contents into csv_content
    csv_content = csv.reader(csv_file, delimiter=',') 

    # pull out the first/header row
    csv_header = next(csv_content)
    
    # (Re)set variables
    total_months = 0
    budget_data = []
    greatest_profit_increase_month = ''
    greatest_profit_decrease_month = ''
    net_profit = 0

    # loop through csv_content by row
    for row in csv_content:

        # append list entry of date (str) and profit (as int) from row into budget_data list 
        budget_data.append([row[0],int(row[1])])
        
        # incement the total number of months included in the dataset by 1
        total_months += 1
            
        # add row[1] to the net total amount of Profit/Losses
        net_profit += int(row[1])

        # check if budget_data len is 1 (ie first loop iteration)
        if len(budget_data) == 1:
            # set first month calculations to 0
            monthly_profit_diff = 0
            monthly_profit_changes_total = 0
            greatest_profit_increase = 0
            greatest_profit_decrease = 0
            
            # set greatest increase and decrease to first month
            greatest_profit_increase_month = row[0]
            greatest_profit_decrease_month = row[0]

        else:
            # calculate the differnce in profit between current and last months, and add to monthly_profit_changes_total
            monthly_profit_diff = int(row[1]) - last_month_profit
            monthly_profit_changes_total += monthly_profit_diff
            
            # check for (and set) current greatest_profit_increase
            if monthly_profit_diff > greatest_profit_increase:
                greatest_profit_increase = monthly_profit_diff
                
                #Set current month for greats profit increase
                greatest_profit_increase_month = row[0]
            
            # check for (and set) current greatest_profit_decrease
            if monthly_profit_diff < greatest_profit_decrease:
                greatest_profit_decrease = monthly_profit_diff
                
                #Set current month for greats profit increase
                greatest_profit_decrease_month = row[0]
                
        # set last_month_profit to row[1] to use in next loop iteration
        last_month_profit = int(row[1])
        
        # show values per loop iteration:
        #print(f'total_months: {total_months}')
        #print(f'last_month_profit: {last_month_profit}')
        #print(f'net_profit: {net_profit}')
        #print(f'monthly_profit_changes_total: {monthly_profit_changes_total}')
        #print(f'greatest_profit_increase: {greatest_profit_increase_month} ({greatest_profit_increase})')
        #print(f'greatest_profit_decrease: {greatest_profit_decrease_month} ({greatest_profit_decrease})\n')


# calculate the average of the changes in Profit/Losses over the entire period.
avg_monthly_change = monthly_profit_changes_total / (total_months - 1) 

#Print results
print('Financial Analysis')
print('--------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${net_profit}')
print(f'Average Change: ${round(avg_monthly_change,2)}')
print(f'Greatest Increase in Profits: {greatest_profit_increase_month} (${greatest_profit_increase})')
print(f'Greatest Decrease in Profits: {greatest_profit_decrease_month} (${greatest_profit_decrease})')

# set output path and file
output_pathfile = Path('./output.txt')
#print(output_pathfile)

# open file object for writing output
with open(output_pathfile, 'w') as outfile:
    # write results to file
    outfile.write('Financial Analysis\n')
    outfile.write('--------------------------\n')
    outfile.write(f'Total Months: {total_months}\n')
    outfile.write(f'Total: ${net_profit}\n')
    outfile.write(f'Average Change: ${round(avg_monthly_change,2)}\n')
    outfile.write(f'Greatest Increase in Profits: {greatest_profit_increase_month} (${greatest_profit_increase})\n')
    outfile.write(f'Greatest Decrease in Profits: {greatest_profit_decrease_month} (${greatest_profit_decrease})')
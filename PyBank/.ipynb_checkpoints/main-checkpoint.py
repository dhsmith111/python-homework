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
    
    # initialize net_profit variable
    net_profit = 0
    # loop through csv_content by row
    for row in csv_content:

        # append list entry of date (str) and profit (as int) from row into budget_data list 
        budget_data.append([row[0],int(row[1])])
        
        # incement the total number of months included in the dataset by 1
        total_months += 1
            
        # add row[1] to the net total amount of Profit/Losses
        net_profit += int(row[1])

        # check if budget_data len is 0 (ie first loop iteration)
        if len(budget_data) == 1:
            # set last_month_profit to row[1] to use in next loop iteration
            last_month_profit = int(row[1])
            
            # and set monthly_profit_changes_total to 0 
            monthly_profit_changes_total = 0
            
            print(f'last_month_profit: {last_month_profit}\nmonthly_profit_changes_total: {monthly_profit_changes_total}')
        else:
            # calculate the differnce in profit between current and last months, and add to monthly_profit_changes_total
            monthly_profit_diff = int(row[1]) - last_month_profit
            monthly_profit_changes_total += monthly_profit_diff

            # and set last_month_profit to row[1] to use in next loop iteration
            last_month_profit = int(row[1])
            print(f'last_month_profit: {last_month_profit}\nmonthly_profit_changes_total: {monthly_profit_changes_total}')


# calculate the average of the changes in Profit/Losses over the entire period.
avg_monthly_change = monthly_profit_changes_total / (total_months - 1) 

# set greatest_increase to 0
greatest_increase = 0

# 
# loop through dates and amounts in budget_data to calculate the greatest increase in profits (date and amount) over the entire period.
for date,amount in budget_data:

# check if amount is larger than greatest_increase, if so set it as new greatest_increase, then set greatest_increase_date to date
    if amount > greatest_increase:
        greatest_increase = amount
        greatest_increase_date = date
                          
# calculate the greatest increase in profits (date and amount) over the entire period.
# calculate the greatest decrease in losses (date and amount) over the entire period

# output results to stdout and to file
print('Financial Analysis')
print('--------------------------------')
print(f'Total Months: {total_months}')
print(f'Total:          ${net_profit}')
print(f'Average Change: ${avg_monthly_change}')
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)


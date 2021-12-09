# Modules
import csv
import os
from statistics import mean

# Files to load and output (Remember to change these)
budget_data = os.path.join("PyBank", "Resources", "budget_data.csv")

# Track various financial parameters
total_months = 0
month_of_change = []
total_net = 0
net_change = 0
net_change_list = []
prev_net = 0
high_profit = 0
low_profit = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]

# Read the csv and convert it into a list of dictionaries

with open(budget_data) as financial_data:
   reader = csv.reader(financial_data)

   # Read the header row
   header = next(reader)

   # Extract first row to avoid appending to net_change_list
   first_row = next(reader)
   total_months += 1
   total_net += int(first_row[1])
   prev_net = int(first_row[1])

   for row in reader:
       # Track the total
       total_months += 1
       total_net += int(row[1])
       net_change = int(row[1]) - prev_net
       prev_net = int(row[1])
       net_change_list += [net_change]
       month_of_change += [row[0]]

       # Calculate the greatest increase
       if net_change > greatest_increase[1]:
           greatest_increase[0] = row[0]
           greatest_increase[1] = net_change

       # Calculate the greatest decrease
       if net_change < greatest_decrease[1]:
           greatest_decrease[0] = row[0]
           greatest_decrease[1] = net_change

average_change = sum(net_change_list) / len(net_change_list)
month_profit_increase = greatest_increase[0] 
profit_increase = greatest_increase[1]
month_profit_decrease = greatest_decrease[0]
profit_decrease = (greatest_decrease[1])

# Generate Output Summary
output = (
   f"Financial Analysis\n"
   f"----------------------------\n"
   f"Total Months: {total_months}\n"
   f"Total: ${total_net}\n"
   f"Average Change: ${average_change}\n"
   f"Greatest Increase in Profits: {month_profit_increase} (${profit_increase})\n"
   f"Greatest Decrease in Profits: {month_profit_decrease} (${profit_decrease})\n"
)

file_to_output = os.path.join("PyBank", "budget_analysis.txt")

print(output)

with open(file_to_output, "w") as txt_file:
   txt_file.write(output)


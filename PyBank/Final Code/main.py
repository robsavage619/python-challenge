# Importing the CSV file
import os
import csv

# Setting path for CSV file
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# Creating empty lists
total_months = []
total_profit = []
monthly_profit_change = []

# Opening the CSV file
with open (csvpath,newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
# Reading the headers
    csv_header = next(csvreader)

# Assigning lists to their respective rows
    for row in csvreader:
        total_months.append(row[0])
        total_profit.append(int(row[1]))

# Running through the list to find profits change/I'm still trying to understand the logic here
    for i in range(len(total_profit)-1):
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])
  
# Grabbing the biggest gains and losses from the previously established profit change list
greatest_increase = max(monthly_profit_change)
greatest_decrease = min(monthly_profit_change)

# Assigning the maxes and mins to their proper months 
greatest_increase_month = monthly_profit_change.index(max(monthly_profit_change)) +1
greatest_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) +1

# Printing Stuff
print("Financial Analysis")
print("-----------------------------------")
print("Total Months: " + str(len(total_months)))
print("Total: $" + str(sum(total_profit))) 
print("Average Change: $" + str(round(sum(monthly_profit_change)/len(monthly_profit_change), 2)))
print("Greatest Increase in Profits: " + str(total_months[greatest_increase_month]+ " ($" + str(greatest_increase)) + ")")
print("Greatest Decrease in Profits: " + str(total_months[greatest_decrease_month]+ " ($" + str(greatest_decrease)) + ")")

#Assign Variables to make exporting easier
avg_change = (round(sum(monthly_profit_change)/len(monthly_profit_change), 2))
gr8_increase = (total_months[greatest_increase_month]+ " ($" + str(greatest_increase)) + ")"
gr8_decrease = ((total_months[greatest_decrease_month]+ " ($" + str(greatest_decrease)) + ")")

# Exporting/Writing to a txt file
pybank_file = os.path.join('..', 'Analysis', 'PyBankTextFile.txt')
with open(pybank_file, 'w') as text_file:
    text_file.write("Financial Analysis")
    text_file.write("\n")
    text_file.write("Total Months: " + str(len(total_months)))
    text_file.write("\n")
    text_file.write("Total: $" + str(sum(total_profit)))
    text_file.write("\n")
    text_file.write("Average Change: $" + str(avg_change))
    text_file.write("\n")
    text_file.write("Greatest Increase in Profits: " + str(gr8_increase))
    text_file.write("\n")
    text_file.write("Greatest Decrease in Profits: " + str(gr8_decrease))
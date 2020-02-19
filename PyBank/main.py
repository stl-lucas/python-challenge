import csv

#Variable Initialization
records = {}
changes = {}
total_months = 0
total_amount = 0
change_amount = 0

#CSV Import and Analysis
csvpath = "budget_data.csv"

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
        #Changes stores kv of date and change amount
        #Records stores kv pair of date and amount
    for row in csvreader:
        changes[row[0]] = int(row[1]) - change_amount
        records[row[0]] = int(row[1])
        change_amount = int(row[1])

#Calculations
for k, v in records.items():
    total_months = total_months + 1
    total_amount = total_amount + v

#Gets the date (key) and amount (value) of the greatest increase
increase_date = max(changes, key=changes.get)
increase_amount = max(changes.values())

#Gets the date (key) and amount (value) of the greatest deccrease
decrease_date = min(changes, key=changes.get)
decrease_amount = min(changes.values())

#Calculates the average change using the changes dictionary. Subracts the first key,value pair since the value of this first
#record should be no change.
average_change = format((sum(changes.values()) - list(records.values())[0]) / (total_months - 1), '.2f')

#Final Print Statement
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_amount}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {increase_date} (${increase_amount})")
print(f"Greatest Decrease in Profits: {decrease_date} (${decrease_amount})")

#Export text file with results
file_1 = open("PyBankResult.txt","w") 
file_1.write("Financial Analysis\n")
file_1.write("----------------------------\n")
file_1.write(f"Total Months: {total_months}\n")
file_1.write(f"Total: ${total_amount}\n")
file_1.write(f"Average Change: ${average_change}\n")
file_1.write(f"Greatest Increase in Profits: {increase_date} (${increase_amount})\n")
file_1.write(f"Greatest Decrease in Profits: {decrease_date} (${decrease_amount})\n")
file_1.close() 
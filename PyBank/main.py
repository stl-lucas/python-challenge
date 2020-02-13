import csv

#Variable Initialization
total_months = 0
total_amount = 0

#CSV Import and Analysis
records = {'Jan-10': 867884, 'Feb-10': 984655, 'Mar-10': 322013, 'Apr-10': -69417 }

#Calculations
for k, v in records.items():
    total_months = total_months + 1
    total_amount = total_amount + v

increase_date = max(records, key=records.get)
increase_amount = max(records.values())
decrease_date = min(records, key=records.get)
decrease_amount = min(records.values())
average_change = format(total_amount / total_months, '.2f')

#Final Print Statement
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_amount}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {increase_date} ({increase_amount})")
print(f"Greatest Decrease in Profits: {decrease_date} ({decrease_amount})")

#Export text file with results
file_1 = open("PyBankResult.txt","w") 
file_1.write("Financial Analysis\n")
file_1.write("----------------------------\n")
file_1.write(f"Total Months: {total_months}\n")
file_1.write(f"Total: ${total_amount}\n")
file_1.write(f"Average Change: ${average_change}\n")
file_1.write(f"Greatest Increase in Profits: {increase_date} ({increase_amount})\n")
file_1.write(f"Greatest Decrease in Profits: {decrease_date} ({decrease_amount})\n")
file_1.close() 
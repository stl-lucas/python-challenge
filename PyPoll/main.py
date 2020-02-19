import csv
import operator

#Variable Assignments
total_votes = 0
candidates = {}

#CSV Import and Analysis
csvpath = "election_data.csv"

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    #Check if candidate exists, if so, add one vote, if not add candidate and set vote to 1
    for row in csvreader:
        key = row[2]
        if key not in candidates:
            candidates[key] = 1
        else:
            candidates[key] += 1
        total_votes = total_votes + 1

#Check to see which key has the highest vote count
winner = max(candidates, key=candidates.get)

#Final Print Statement
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")

#for each candidate in list
for k, v in candidates.items():
    percent = format(int(v) / total_votes * 100, '.3f')
    print("{0}: {2}% ({1})".format(k, v, percent))
#end for

print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")

#Export text file with results
file_1 = open("PyPollResult.txt","w") 
file_1.write("Election Results\n")
file_1.write("----------------------------\n")
file_1.write(f"Total Votes: {total_votes}\n")
file_1.write("----------------------------\n")

for k, v in candidates.items():
    percent = format(int(v) / total_votes * 100, '.3f')
    file_1.write("{0}: {2}% ({1})\n".format(k, v, percent))

file_1.write("----------------------------\n")
file_1.write(f"Winner: {winner}\n")
file_1.write("----------------------------\n")
file_1.close() 
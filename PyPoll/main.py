import operator

#Variable Assignments
total_votes = 0
votes = {'Khan': 2218231, 'Correy': 704200, 'Li': 492940, 'O\'Tooley': 105630 }

#CSV Import and Analysis
winner = max(votes, key=votes.get)

#Calculations
for k, v in votes.items():
    total_votes = total_votes + v

#Final Print Statement
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")

#for each candidate in list
for k, v in votes.items():
    percent = format(v / total_votes * 100, '.3f')
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

for k, v in votes.items():
    percent = format(v / total_votes * 100, '.3f')
    file_1.write("{0}: {2}% ({1})\n".format(k, v, percent))

file_1.write("----------------------------\n")
file_1.write(f"Winner: {winner}\n")
file_1.write("----------------------------\n")
file_1.close() 
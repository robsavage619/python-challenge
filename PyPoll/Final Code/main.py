# Importing the CSV file
import os
import csv

# Setting path for CSV file
csvpath = os.path.join('..', 'Resources', 'election_data.csv')

# Creating empty lists for variables and zeroing them out
voter_id = []
county = []
candidates = []
khan = []
correy = []
li = []
otooley = []
khan_votes = 0 
correy_votes = 0
li_votes = 0
otooley_votes = 0
total_votes = 0
winner = 0

# Opening the CSV file
with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
# Reading the headers
    csv_header = next(csvreader)

# Attaching lists to rows 
    for row in csvreader: 
        voter_id.append(int(row[0]))
        county.append(str(row [1]))
        candidates.append(str(row[2]))
    
# Counting the number of votes
    total_votes = (len(voter_id))

# Individual Votes
    for i in candidates:
        if i == "Khan":
            khan.append(candidates)
            khan_votes = len(khan)
        elif i == "Correy":
            correy.append(candidates)
            correy_votes = len(correy)
        elif i == "Li":
            li.append(candidates)
            li_votes = len(li)
        else:
            otooley.append(candidates)
            otooley_votes = len(otooley)

# Calculating percentages
    khan_percentage = round((khan_votes/total_votes) * 100, 2)
    correy_percentage = round((correy_votes/total_votes) * 100, 2)
    li_percentage = round((li_votes/total_votes) * 100, 2)
    otooley_percentage = round((otooley_votes/total_votes) * 100, 2)
 
# Finding the winner
    if khan_percentage > max(correy_percentage, li_percentage, otooley_percentage):
        winner = "Khan"
    elif correy_percentage > max(khan_percentage, li_percentage, otooley_percentage):
        winner = "Correy"
    elif li_percentage > max(khan_percentage, correy_percentage, otooley_percentage):
        winner = "Li"
    else: 
        winner = "O'Tooley"

# Printing Stuff
print("Election Results")
print("----------------------------")
print("Total Votes: " + str(total_votes))
print("----------------------------")
print("Khan: " + str(khan_percentage) + "% " + str(khan_votes))
print("Correy: " + str(correy_percentage) + "% " + str(correy_votes)) 
print("Li: " + str(li_percentage) + "% " + str(li_votes))
print("O'Tooley: " + str(otooley_percentage) + "% " + str(otooley_votes))
print("----------------------------")
print("Winner: " + str(winner))
print("----------------------------")

# Exporting/Writing to a txt file
pypoll_file = os.path.join('..', 'Analysis', 'PyPollTextFile.txt')
with open(pypoll_file, 'w') as text_file:
    text_file.write("Election Results")
    text_file.write("\n")
    text_file.write("----------------------------")
    text_file.write("\n")
    text_file.write("Total Votes: " + str(total_votes))
    text_file.write("\n")
    text_file.write("----------------------------")
    text_file.write("\n")
    text_file.write("Khan: " + str(khan_percentage) + "% " + str(khan_votes))
    text_file.write("\n")
    text_file.write("Correy: " + str(correy_percentage) + "% " + str(correy_votes))
    text_file.write("\n")
    text_file.write("Li: " + str(li_percentage) + "% " + str(li_votes))
    text_file.write("\n")
    text_file.write("O'Tooley: " + str(otooley_percentage) + "% " + str(otooley_votes))
    text_file.write("\n")
    text_file.write("----------------------------")
    text_file.write("\n")
    text_file.write("Winner: " + str(winner))
    text_file.write("\n")
    text_file.write("----------------------------")
   



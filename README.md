# Python Financial and Election Analysis 

![Revenue](Images/revenue-per-lead.png)

---

![Visualization](Images/python-gif.gif "Code Walkthrough")

---

## Contact Information

Rob Savage 

rob.savage@me.com

[LinkedIn](https://www.linkedin.com/in/robsavage/)


[Tableau Public](https://public.tableau.com/profile/rob.savage)

---

## Project Description

The purpose of this project was to use two different data sets in two separate projects to make inferences about the respective data. PyBank's task was to create a Python script to handle the following objectives:

  - The total number of months included in the dataset


  - The net total amount of "Profit/Losses" over the entire period


  - The average of the changes in "Profit/Losses" over the entire period


  - The greatest increase in profits (date and amount) over the entire period


  - The greatest decrease in losses (date and amount) over the entire period


For PyPoll the objective was to create a Python script to analyze election data with the following objectives:

  - The total number of votes cast


  - A complete list of candidates who received votes


  - The percentage of votes each candidate won


  - The total number of votes each candidate won


  - The winner of the election based on popular vote.

---

## Tools Used

1. Python (Data Aggregation)

2. Github (Publishing of Results and Analysis)

3. Atom

4. CSV

5. OS

---

## Steps PyBank

1. Used `Python` to aggregate data from the `budget_data.csv` in the `Resources` folder

 - Created empty lists (`total_months`, `total_proft`, and `monthly_profit_change`) to hold the my data 
 - Read in the `CSV`, along with the headers
 - Appended the data to their appropriate lists
 - Calculated `monthly_profit_change`
 - Created variables to hold the min and max profit changes
 - Printed the results
 - Exported the results to a txt files

---

## Steps PyPoll

1. Used `Python` to aggregate data from the `election_data.csv` in the `Resources` folder

 - Created empty lists (`voter_id`, `county`, `candidates`, `khan`, `correy`, `li`, `otooley`, `khan_votes`, `correy_votes`, `li_votes`, `otooley_votes`, `total_votes`, and `winner`) to hold the my data 
 - Read in the `CSV`, along with the headers
 - Appended the data to their appropriate lists
 - Calculated `total_votes` via `len` of the `voter_id` column
 - Created `for`loops that matched the candidates last name and appended the data to their respective lists
 - Calculated vote percentages by running each of the candidates votes against the total votes
 - Printed the results
 - Exported the results to a txt files

---

## Analysis

PyBank - 

Total Months: 86

Total: $38382578

Average Change: $-2315.12

Greatest Increase in Profits: Feb-2012 ($1926159)

Greatest Decrease in Profits: Sep-2013 ($-2196167)


PyPoll - 

Total Votes: 3521001

Khan: 63.0% 2218231

Correy: 20.0% 704200

Li: 14.0% 492940

O'Tooley: 3.0% 105630

Winner: Khan

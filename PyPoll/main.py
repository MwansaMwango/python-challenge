import os
import csv

#Initiatialise variables
totalVotes = 0
khanVotes = 0 
correyVotes = 0
liVotes = 0
otooleyVotes = 0
khanVotesPercentage = 0
correyVotesPercentage = 0
liVotesPercentage = 0
otooleyVotesPercentage = 0
winner = 0

#Get file handler
filePath = os.path.join("Resources", "election_data.csv")
election_results = {"Khan": 0, "Correy":0,"Li":0,"O'Tooley":0}

#Get total number of rows
with open(filePath) as csvfile:
    #Create file reader object
    csvreader = csv.reader(csvfile, delimiter=',')
    #Ignore first row / header
    header = next(csvreader)

#With the open file, perform required manipulations and clean up after
with open(filePath) as csvfile:    
    #Create file reader object
    csvreader = csv.reader(csvfile, delimiter=',')
    #Ignore first row / header
    header = next(csvreader)
    for row in (csvreader):
  
        #Count each vote using row / iteration 
        totalVotes += 1
        
        #Check candidate voted for and add 1 to their vote count
        if row[2] == "Khan":
            khanVotes += 1
            election_results["Khan"] = khanVotes
        elif row[2] == "Correy":
            correyVotes += 1
            election_results["Correy"] = correyVotes
        elif row[2] == "Li":
            liVotes += 1
            election_results["Li"] = liVotes
        elif row[2] == "O'Tooley":
            otooleyVotes += 1
            election_results["O'Tooley"] = otooleyVotes
        
    #Calculate vote percentages for each candidate 
    khanVotesPercentage = round(float((khanVotes / totalVotes)*100),3)
    correyVotesPercentage = round(float((correyVotes / totalVotes)*100),3)
    liVotesPercentage = round(float((liVotes / totalVotes)*100),3)
    otooleyVotesPercentage = round(float((otooleyVotes / totalVotes)*100),3)

    #Calculate Winner by getting maximum key value
    winner = max(election_results, key=election_results.get)
    

file_data = f'''
Election Results
-------------------------
Total Votes: {totalVotes}
-------------------------
Khan: {khanVotesPercentage}% ({khanVotes})
Correy: {correyVotesPercentage}% ({correyVotes})
Li: {liVotesPercentage}% ({liVotes})
O'Tooley: {otooleyVotesPercentage}% ({otooleyVotes})
-------------------------
Winner: {winner}
-------------------------
'''

print(file_data)

#Specifiy output file and path
data_output = os.path.join("Analysis","pyPoll_analysis.txt")

#Write data to a new txt file
with open(data_output, "w") as txtfile:
    txtfile.write(file_data)



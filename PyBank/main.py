import os
import csv

#Initiatialise variables
totalMonths = 0
netProfit = 0 
greatestIncrease = 0
greatestDecrease = 0
greatestIncreaseDate = 0
greatestDecreaseDate = 0
totalProfitChange = 0
previousProfit = 0
initialProfit = 0
finalProfit = 0
row_count = 0

#Get file handler
filePath = os.path.join("Resources", "budget_data.csv")

#Get total number of rows
with open(filePath) as csvfile:
    #Create file reader object
    csvreader = csv.reader(csvfile, delimiter=',')
    #Ignore first row / header
    header = next(csvreader)
    row_count = len(csvfile.readlines())

#With the open file, perform required manipulations and clean up after
with open(filePath) as csvfile:    
    #Create file reader object
    csvreader = csv.reader(csvfile, delimiter=',')
    #Ignore first row / header
    header = next(csvreader)
    for index, row in enumerate(csvreader):
  
        #Get initial and final profit to calculate average profit change
        if index == 0:
            initialProfit = float(row[1])
        elif index == row_count-1:
            finalProfit = float(row[1])
 
        #Count each month using row / iteration count must equal = 86
        totalMonths += 1
        
        #Add the row[1] to netProfit over entire period
        netProfit = netProfit + int(row[1])

        #Find profitChange
        profitChange = float(row[1]) - previousProfit
        
        #Update totalProfitChange
        totalProfitChange += profitChange

        #Find Greatest Increase and Decrease
        if profitChange >= greatestIncrease:
            greatestIncrease = profitChange
            greatestIncreaseDate = row[0]
        elif profitChange <= greatestDecrease:
            greatestDecrease = profitChange
            greatestDecreaseDate = row[0]
       
        #Record new last profit
        previousProfit = float(row[1])

    #Calculate average change 
    avgProfitChange = round(float((finalProfit - initialProfit) / (totalMonths - 1)),2)
    


file_data = f'''
Financial Analysis
----------------------------
Total Months: {totalMonths}
Total: ${netProfit}
Average  Change: ${avgProfitChange}
Greatest Increase in Profits: {greatestIncreaseDate} ($ {greatestIncrease})
Greatest Decrease in Profits: {greatestDecreaseDate} ($ {greatestDecrease})
'''

print(file_data)

#Specifiy output file and path
data_output = os.path.join("Analysis","pyBank_analysis.txt")

#Write data to a new txt file
with open(data_output, "w") as txtfile:
    txtfile.write(file_data)



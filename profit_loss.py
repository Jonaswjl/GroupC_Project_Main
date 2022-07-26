from pathlib import Path 
import csv

# instantiate a file path to the profit and loss csv file 
file_path = Path.cwd()/"csv_reports2"/"profit and loss.csv"

# create an empty list to append net profit to
net_profit=[]

# open file in read mode 
with file_path.open(mode="r",encoding="UTF-8-sig", newline="") as file: 
    # create a reader object
    reader = csv.reader(file)
    # skip the headers
    next(reader)
    # append values of net profit to empty list
    for line in reader:
        net_profit.append(int(line[4]))
    #for day 6 i cannot add 1 to create a day 7 so must -1
    for i in range(len(net_profit)-1):
        diff=(net_profit[i+1]-net_profit[i])
        # checks whether difference between days is a negative number, return absolute value of the difference so its not a negative number
        if diff < 0: 
            print(f"[PROFIT DEFICIT] AMOUNT: {abs(diff)}")
        else: 
            print(f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")



    
    






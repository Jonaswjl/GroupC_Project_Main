from pathlib import Path 
import csv

file_path = Path.cwd()/"csv_reports2"/"profit and loss.csv"

net_profit=[]
dailydiff=[]
with file_path.open(mode="r",encoding="UTF-8-sig", newline="") as file: 
    reader = csv.reader(file)
    next(reader)
    for line in reader:
        net_profit.append(int(line[4]))

def profit():
    i=0
    while i < (len(net_profit)-1):
        if net_profit[i] < net_profit[i+1]:
            message="Net profit of each day is higher than the previous day"
            return message 
        else:
            diff= net_profit[i]-net_profit[i+1]
            print(diff) 


            



    
    






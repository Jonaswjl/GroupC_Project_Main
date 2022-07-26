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
    #for day 6 i cannot add 1 to create a day 7 so must -1
    for i in range(len(net_profit)-1):
        diff=(net_profit[i+1]-net_profit[i])
        if diff < 0: 
            print(f"[PROFIT DEFICIT] AMOUNT: {diff}")
        else: 
            print(f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
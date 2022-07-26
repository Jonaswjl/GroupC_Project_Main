from pathlib import Path 
import csv

file_path = Path.cwd()/"csv_reports2"/"profit and loss.csv"

net_profit=[]
dailydiff=[]
with file_path.open(mode="r",encoding="UTF-8-sig", newline="") as file: 
    reader = csv.reader(file)
    next(reader)
    for line in reader:
        net_profit.append([float(line[0])]+[float(line[4])])
print(net_profit)
def profit():
    for values in net_profit:
        i=0
        while i < (len(net_profit)-1):
            if values[i] < values[i+1]:
                diff= values[i+1]-values[i]
                message= f"DAY: {values[i]}, AMOUNT: SGD{diff}"
                return message
            else:
                message="Net profit of each day is higher than the previous day"
                return message 

print(profit())
            



    
    






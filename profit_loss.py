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
        






from pathlib import Path 
import csv 

file_path = Path.cwd()/"csv_reports"/"cash-on-hand-thb.csv"
print(file_path.exists())
with file_path.open(mode="r",encoding="UTF-8-sig",newline="") as file: 
    reader = csv.reader(file)
    for line in reader: 
        print(line)
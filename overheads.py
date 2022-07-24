from pathlib import Path 
import csv 

# instantiate a file path to overheads csv file in current working directory 
file_path = Path.cwd()/"csv_reports2"/"overheads.csv"

# open the csv file in read mode 
with file_path.open(mode="r",encoding="UTF-8",newline="") as file: 
    # create a reader object 
    reader = csv.reader(file)
    # print the contents of the csv file 
    for line in reader: 
        print(line)
        print(line[1])
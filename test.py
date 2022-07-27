## cash on hand 
from pathlib import Path 
import csv 

# create an empty list to store cash on hand values 
coh = []

# instantiate a file path to the cash on hand csv file 
file_path = Path.cwd()/"csv_reports"/"cash-on-hand-thb.csv"
# open file in read mode
with file_path.open(mode="r",encoding="UTF-8",newline="") as file: 
    # create a reader object
    reader = csv.reader(file)
    # skip headers 
    # next(reader)
    # append cash on hand to list 
    for line in reader:
        print(line[0])
    #     coh.append(int(line[1]))
    # for i in range(len(coh)-1):
    #     diff=(coh[i+1]-coh[i])
    #     # checks whether difference between days is a negative number, return absolute value of the difference so its not a negative number
    #     if diff < 0: 
    #         print(f"[CASH DEFICIT] AMOUNT: {abs(diff)}")
    #     else: 
    #         print(f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")

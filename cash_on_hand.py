## cash on hand 
from pathlib import Path 
import csv
from pickle import FALSE, TRUE 

coh=[]
dd=[]
d=[]
file_path = Path.cwd()/"csv_reports"/"cash-on-hand-thb.csv"
# open file in read mode 
with file_path.open(mode="r",encoding="UTF-8", newline="") as file: 
    # create a reader object
    reader = csv.reader(file)
    # skip the headers
    next(reader)
    for line in reader:
        # append only the net profits for each day to the empty list and convert them to floats (so diff can be calculated)
        coh.append(float(line[1]))
        d.append(line[0])

day=(len(coh)-1)  
# i is an index (eg 0-5) range gives 0 to the highest index (in this case 6 days will have indices 0-5 )
for i in range(day):
    diff=(coh[i+1]-coh[i])
    # append the list of days and list of differences
    # combine the day no. when there is a profit deficit with the diff in a nested list
    dd.append([d[i+1]]+[diff])

#convert nested list into a dictionary where day number is the key and profit difference is the value 
dict=dict(dd)
print(dict)
is_positive= TRUE
for pd in dict:
    #dict[pd] accesses the values (profit diff) and pd is the key 
    if dict[pd] < 0: 
        print(f"[CASH DEFICIT] DAY: {pd} AMOUNT: SGD{abs(dict[pd])}")
        is_positive= FALSE   
# This else executes only if the break never happens
if is_positive==TRUE:
    print(f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
    
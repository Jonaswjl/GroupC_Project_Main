## cash on hand 
from pathlib import Path 
import csv 

# # create an empty list to store cash on hand values 
# coh = []

# # instantiate a file path to the cash on hand csv file 
# file_path = Path.cwd()/"csv_reports"/"cash-on-hand-thb.csv"
# # open file in read mode
# with file_path.open(mode="r",encoding="UTF-8",newline="") as file: 
#     # create a reader object
#     reader = csv.reader(file)
#     # skip headers 
#     next(reader)
#     # append cash on hand to list 
#     for line in reader:
#         coh.append(float(line[1]))
#     for i in range(len(coh)-1):
#         diff=(coh[i+1]-coh[i])
#         # checks whether difference between days is a negative number, return absolute value of the difference so its not a negative number
#         if diff < 0: 
#             print(f"[CASH DEFICIT] AMOUNT: SGD{abs(diff)}")
#     else: 
#             print(f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")

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
for pd in dict:
    #dict[pd] accesses the values (profit diff) and pd is the key 
    if dict[pd] < 0: 
        print(f"[CASH DEFICIT] DAY: {pd} AMOUNT: SGD{abs(dict[pd])}")
        #if the condition above is met the for loop breaks 
        break
# This else executes only if the break never happens
else: 
    print(f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
    
        
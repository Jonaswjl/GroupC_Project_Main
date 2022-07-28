from pathlib import Path 
import csv


# instantiate a file path to the profit and loss csv file 
file_path = Path.cwd()/"csv_reports2"/"profit and loss.csv"

# create an empty list to append net profit 
net_profit=[]
# create an empty list to append the day and difference of net profit 
dd=[]
d=[]
# open file in read mode 
with file_path.open(mode="r",encoding="UTF-8", newline="") as file: 
    # create a reader object
    reader = csv.reader(file)
    # skip the headers
    next(reader)
    for line in reader:
        # append only the net profits for each day to the empty list and convert them to floats (so diff can be calculated)
        net_profit.append(float(line[4]))
        d.append(line[0])

day=(len(net_profit)-1)  
# i is an index (eg 0-5) range gives 0 to the highest index (in this case 6 days will have indices 0-5 )
for i in range(day):
    diff=(net_profit[i+1]-net_profit[i])
    # append the list of days and list of differences
    # combine the day no. when there is a profit deficit with the diff in a nested list
    dd.append([d[i+1]]+[diff])

#convert nested list into a dictionary where day number is the key and profit difference is the value 
dict=dict(dd)
print(dict)
for pd in dict:
    #dict[pd] accesses the values (profit diff) and pd is the key 
    if dict[pd] < 0: 
        print( f"[PROFIT DEFICIT] DAY: {pd} AMOUNT: SGD{abs(dict[pd])}")
        #if the condition above is met the for loop breaks 
        break
# This else executes only if the break never happens
else: 
    print( f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")

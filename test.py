from pathlib import Path 
import csv, math

# instantiate a file path to the profit and loss csv file 

# file_path = Path.cwd()/"csv_reports"/"profit-and-loss-thb.csv"
file_path = Path.cwd()/"csv_reports2"/"profit and loss.csv"

# create an empty list to append net profit to
net_profit=[]
days=[]
list=[]
diff_list=[]
# open file in read mode 
with file_path.open(mode="r",encoding="UTF-8", newline="") as file: 
    # create a reader object
    reader = csv.reader(file)
    # skip the headers
    next(reader)
    # append values of net profit to empty list
    for line in reader:
        net_profit.append(float(line[4]))
        line.pop(1)
        # print(line)
        line.pop(1)
        # print(line)
        line.pop(1)
        # print(line)
        line.sort()
        list.append(line)


        
# print(f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
# print(f"[PROFIT DEFICIT] AMOUNT: SGD{abs(diff)}")


    
    



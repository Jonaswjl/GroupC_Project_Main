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
    day=(len(net_profit)-1)   
    for i in range(day):
        diff=(net_profit[i+1]-net_profit[i])
        diff_list.append(diff)
        # check through all the difference and see if they are all greater than 0
        list_prod = math.prod(diff_list)
        
diff=(net_profit[i+1]-net_profit[i])
for i in range(day):
    # if all the differences are greater than 0, return a single statement which states that all the differences are greater than 0 
    if list_prod > 0: 
        print(f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
        break
    # # if not all differences are greater than 0 return the amounts which are less than 0
    elif list_prod < 0: 
        
        


    # if not all differences are greater than 0 return the amounts which are less than 0
        
# print(f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
# print(f"[PROFIT DEFICIT] AMOUNT: SGD{abs(diff)}")


    
    



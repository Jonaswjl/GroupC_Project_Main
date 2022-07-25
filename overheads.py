from pathlib import Path 
import csv 

# def overhead_function(): 
list = []

category = []
overheads = []

# instantiate a file path to overheads csv file in current working directory 
file_path = Path.cwd()/"csv_reports"/"overheads-day-45.csv"

# open the csv file in read mode 
with file_path.open(mode="r",encoding="UTF-8-sig",newline="") as file: 
    # create a reader object 
    reader = csv.reader(file)
    next(reader)
    for line in reader:
        category.append(line[0])
        overheads.append(float(line[1]))
        line.sort()
        # print(line)
        list.append(line)
# print(list)
dict = dict(list)
        
# print(category)
max = max(overheads)
key = str(max)
# print(type(key))
# print(dict[key])

print(f"[Highest Overheads] {dict[key]}: SGD{key}")


#         # convert the numbers from string to float 
#         overheads.append(float(line[1]))
# print(overheads)
# # sort the numbers in descending order
# overheads.sort(reverse=True)
# print(overheads)
# # print the largest number which is the highest overhead cost
# print(overheads[0])




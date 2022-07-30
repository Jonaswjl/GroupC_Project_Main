def coh_function(): 
    from pathlib import Path 
    import csv
    import api 

    forex = api.rate_function()

    coh=[]
    dd=[]
    d=[]
    file_path = Path.cwd()/"csv_reports_game"/"cash-on-hand-usd-42.csv"
    # file_path = Path.cwd()/"csv_reports2"/"cash on hand.csv"
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
    dictionary =dict(dd)
    is_positive= True
    for pd in dictionary:
        #dict[pd] accesses the values (profit diff) and pd is the key 
        if dictionary[pd] < 0: 
            print(f"[CASH DEFICIT] DAY: {pd} AMOUNT: SGD{round(((dictionary[pd])*forex*-1),1)}")
            is_positive= False 
    if is_positive==True:
        print(f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")


    
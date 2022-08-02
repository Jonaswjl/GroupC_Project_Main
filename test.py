
result = []
import requests 
## Alpha vantage API Key 
api_key = "1H49MTNIA7TNIJLO"

## Calling API from python 
url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"

response = requests.get(url)
data = response.json()
# print outer key
# for key in data.keys(): 
#     print(key)
# # print all the inner keys 
# for keys in data['Realtime Currency Exchange Rate'].keys(): 
#     print(keys)
# assign outer key to variable 
outer_key = 'Realtime Currency Exchange Rate'
# check whether outer key is in data
if outer_key in data: 
    try: 
        rate=data['Realtime Currency Exchange Rate']['5. Exchange Rate']
        # rate = float(rate)
        result.append(rate)
        print(result)
    except KeyError: 
        pass
else: 
    print(data["Note"])
    print(type(data))


from pathlib import Path
file_path = Path.cwd()/"test.txt"
if file_path.exists(): 
    with file_path.open(mode="w",encoding="UTF-8") as file:
        file.writelines(result)
else: 
    print("file doesn't exist")

    






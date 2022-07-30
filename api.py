# create a function to find the exchange rate between SGD and USD
def api_function(): 
    import requests 
    ## Alpha vantage API Key 
    api_key = "1H49MTNIA7TNIJLO"

    ## Calling API from python 
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"

    response = requests.get(url)
    data = response.json()
    # rate = data['Realtime Currency Exchange Rate']['5. Exchange Rate']
    for info in data:
        rate=data[info]['5. Exchange Rate']
    rate = float(rate)
    print(f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{rate}")

def rate_function():
    import requests 
    ## Alpha vantage API Key 
    api_key = "1H49MTNIA7TNIJLO"

    ## Calling API from python 
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"

    response = requests.get(url)
    data = response.json()
    for info in data:
        rate=data[info]['5. Exchange Rate']
    # rate = data['Realtime Currency Exchange Rate']['5. Exchange Rate']
    rate = float(rate)
    return rate

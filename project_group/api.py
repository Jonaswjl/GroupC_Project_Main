def api_function(): 
    try: 
        import requests 
        ## Alpha vantage API Key 
        api_key = "1H49MTNIA7TNIJLO"

        ## Calling API from python 
        url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"

        response = requests.get(url)
        data = response.json()
        rate=data['Realtime Currency Exchange Rate']['5. Exchange Rate']
        rate = float(rate)
        return f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{rate}"
    except KeyError: 
        return data["Note"]

def rate_function(): 
    try: 
        import requests 
        ## Alpha vantage API Key 
        api_key = "1H49MTNIA7TNIJLO"

        ## Calling API from python 
        url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"

        response = requests.get(url)
        data = response.json()
        rate= data['Realtime Currency Exchange Rate']['5. Exchange Rate']
        rate = float(rate)
        return rate
    except KeyError:
        return data["Note"]



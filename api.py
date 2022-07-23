# create a function to find the exchange rate between SGD and USD
def api_function(): 
    import requests 
    ## Alpha vantage API Key 
    api_key = "1H49MTNIA7TNIJLO"

    ## Calling API from python 
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"

    response = requests.get(url)
    print(response)
    data = response.json()
    print(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])
api_function()
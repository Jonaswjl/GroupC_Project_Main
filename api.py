import requests 

response = requests.get("http://data.gov.sg")
print(response.headers.get("content-type"))
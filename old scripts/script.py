import requests
import json

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&apikey=demo'
r = requests.get(url)
data = r.json()

print(data)
json_str = json.dumps(data, indent=4)

# Print the pretty-printed JSON string
print(json_str)



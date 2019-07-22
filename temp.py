import requests

api_key = 'BdIOkholVxjBXxOuZIxEaKukahz9JpCh'
secret_key = 'RZxHeNDqOn+IsOHwFU7yqSJ3DWlvTtWO'
response = requests.get('https://api.hitbtc.com/api/2/trading/balance',
                        auth=(api_key, secret_key))
for i in response.json():
    if i['currency'] == 'USD':
        print(i)

from email import header
import requests
import json

headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }

response = requests.get('https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=json&date=&selectType=&_=1662211678198',
    headers = headers,
    timeout = 5
)

print(response.json()['data'])
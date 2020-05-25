from requests import Request, Session
import json
import re

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '3d2a15de-41c1-4149-b516-2f9ee70155ff',
}

session = Session()
session.headers.update(headers)

def parse_text(text):
    pattern = r'/\w+'
    crypto = re.search(pattern, text).group()
    print(crypto)
    return crypto[1:]


def write_json(data, filename='answer.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    write_json(data)
except:
    print('bad')

def main():
    if parse_text('сколько стоит /bitcoin?') == 'bitcoin':
        price = data['data'][0]['quote']['USD']['price']
        print(price)

main()

from flask import Flask
from flask import request, jsonify
import requests
from requests import Request, Session
import json
from flask_sslify import SSLify



app = Flask(__name__)
sslify = SSLify(app)

URL = 'https://api.telegram.org/bot1225815659:AAESr7yWXzXmokbQjSbrJ-dLcMCFzmzgsiI/'

def write_json(data, filename='answer.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def send_message(chat_id, text='bla-bla-bla'):
    url = URL + 'sendMessage'
    answer = {'chat_id': chat_id, 'text': text}
    r = requests.post(url, json=answer)
    return r.json()


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        r = request.get_json()
        chat_id = r['message']['chat']['id']
        message = r['message']['text']

        if 'bitcoin' in message:
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
            try:
                response = session.get(url, params=parameters)
                data = json.loads(response.text)
                write_json(data)
            except:
                print('bad')
            price = str(data['data'][0]['quote']['USD']['price'])
            send_message(chat_id, price)
        #write_json(r)
        return jsonify(r)
    return 'hello bot!'


#https://api.telegram.org/bot1225815659:AAESr7yWXzXmokbQjSbrJ-dLcMCFzmzgsiI/setWebhook?url=https://b72e0dd6.ngrok.io/
#https://api.telegram.org/bot1225815659:AAESr7yWXzXmokbQjSbrJ-dLcMCFzmzgsiI/deleteWebhook
if __name__ == '__main__':
    #main()
    app.run()

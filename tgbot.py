import pprint

import requests

token = '7139186900:AAFpFW6RyfRoCxm45I5KVMOE_7D6VzsRF4U'
main_url = f'https://api.telegram.org/bot{token}'
# url = f'{main_url}/getMe'
#
# result = requests.get(url)
# print(result.json())

url = f'{main_url}/getUpdates'
result = requests.get(url)
pprint.pprint(result.json())

messages = result.json()["result"]
for message in messages:
    chat_id = message['message']['chat']['id']
    url = f'{main_url}/setMessage'
    params = {
        'chat_id': chat_id,
        'text': 'прлнощзрнлкзщр'
    }
    result = requests.post(url,params=params)
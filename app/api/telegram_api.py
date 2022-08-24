import os

import requests


def send_to_user(text, chat_id):
    token = os.getenv("TELEGRAM_BOT")
    url = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + str(chat_id) + '&text=' + text
    response = requests.post(url)
    print(response.json())
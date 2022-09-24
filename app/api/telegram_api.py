

import requests

from app.configuration.config import TELEGRAM_BOT


def send_to_user(text, chat_id):
    url = 'https://api.telegram.org/bot' + TELEGRAM_BOT + '/sendMessage?chat_id=' + str(chat_id) + '&text=' + text
    response = requests.post(url)
    print(response.json())
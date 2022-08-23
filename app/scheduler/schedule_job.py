import threading
import time

import schedule

from app.service.get_sell_recommentation_service import sell_recommendation
from app.service.sync_price_data_service import sync_price_data


def do_data_fetch_job():
    sync_price_data()


def do_get_sell_recommendation():
    MY_CHAT_ID = '473199101'
    sell = sell_recommendation(MY_CHAT_ID)
    print(sell)


def run_continuously(interval=1):
    while True:
        schedule.run_pending()
        time.sleep(interval)


def run_job():
    schedule.every().day.at("16:30").do(do_data_fetch_job)
    schedule.every().day.at("17:00").do(do_get_sell_recommendation)
    t1 = threading.Thread(target=run_continuously, args=[])
    t1.start()

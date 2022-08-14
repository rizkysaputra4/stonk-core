import threading
import time

import schedule

from app.service.sync_price_data import sync_price_data


def do_data_fetch_job():
    sync_price_data()


def run_continuously(interval=1):
    while True:
        schedule.run_pending()
        time.sleep(interval)


def run_job():
    schedule.every().day.at("16:00").do(do_data_fetch_job)
    t1 = threading.Thread(target=run_continuously, args=[])
    t1.start()

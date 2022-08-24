import threading
import time

import schedule

from app.api.telegram_api import send_to_user
from app.repository.portfolio_repository import get_distinct_user_id
from app.service.get_sell_recommentation_service import sell_recommendation
from app.service.sync_price_data_service import sync_price_data


def do_data_fetch_job():
    sync_price_data()


def do_get_sell_recommendation():
    list_user = get_distinct_user_id()
    if not list_user: return
    for v in list_user:
        sell = sell_recommendation(v)
        if not sell: continue
        out = "Sell Recommendation: "
        for i, sell_tick in enumerate(sell):
            out += f"\n{i+1}. {sell_tick}"
        send_to_user(out, str(v))


def run_continuously(interval=1):
    while True:
        schedule.run_pending()
        time.sleep(interval)


def run_job():
    schedule.every().day.at("16:30").do(do_data_fetch_job)
    schedule.every().day.at("17:00").do(do_get_sell_recommendation)
    t1 = threading.Thread(target=run_continuously, args=[])
    t1.start()

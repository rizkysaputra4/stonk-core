from datetime import datetime, timedelta

from app.repository.price_repository import get_price_history
from app.repository.ticker_repository import get_lq45_ticker


def get_recommendation():
    one_year_ago = (datetime.now() - timedelta(days=368)).strftime('%Y-%m-%d')
    df_one_year_ago = get_price_history('BMRI', one_year_ago)
    lq45_list = get_lq45_ticker()
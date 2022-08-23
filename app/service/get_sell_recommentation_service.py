from datetime import timedelta, datetime

from app.repository.portfolio_repository import get_active_action
from app.repository.price_repository import get_price_history
from app.service.get_recommendation_service import get_price_since


def sell_recommendation(user_id) -> object:
    active_action = get_active_action(user_id)
    result_sell = set()
    one_year_ago = (datetime.now() - timedelta(days=368)).strftime('%Y-%m-%d')
    for tick in active_action:
        if tick.ticker in result_sell:
            continue
        df = get_price_history(tick.ticker, one_year_ago)
        df_merged = get_price_since(df)
        if is_break_sell(df_merged):
            result_sell.add(tick.ticker)
    return list(result_sell)


def is_break_sell(df):
    today_price = df.tail(1).iloc[0]
    is_today_down = today_price['close'] < today_price['moving_average'] and today_price['close'] < today_price[
        'exponential_moving_average']
    return is_today_down

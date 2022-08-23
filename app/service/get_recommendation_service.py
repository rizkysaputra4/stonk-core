from datetime import datetime, timedelta

import pandas as pd
import talib

from app.model.dto.action_point import ActionPoint
from app.model.dto.backtest_result import BackTestResult
from app.repository.price_repository import get_price_history
from app.repository.ticker_repository import get_lq45_ticker
from app.service.back_test_service import get_estimated_profit

MA_PERIOD = 50
EMA_PERIOD = 8
CUT_BY = MA_PERIOD if MA_PERIOD > EMA_PERIOD else EMA_PERIOD


def get_recommendation():
    ten_year_ago = (datetime.now() - timedelta(days=5475)).strftime('%Y-%m-%d')
    one_year_ago = (datetime.now() - timedelta(days=368)).strftime('%Y-%m-%d')
    lq45_list = get_lq45_ticker()
    btr_list = []
    for tick in lq45_list:
        df = get_price_history(tick.ticker, one_year_ago)
        if df.empty: continue
        df_merged = get_price_since(df)
        if df_merged.empty: continue
        if is_break_buy(df_merged):
            df = get_price_history(tick.ticker, ten_year_ago)
            df_ten_year = get_price_since(df)
            action_point = get_action_point(df_ten_year)
            estimated_profit = get_estimated_profit(df_ten_year, action_point)
            btr = BackTestResult(ticker=tick.ticker, profit=estimated_profit[0], hit=estimated_profit[1])
            btr_list.append(btr)
            btr_list.sort(key=lambda x: x.profit, reverse=True)
    print(btr_list)
    return btr_list


def get_price_since(df):
    ma = talib.MA(df['close'], timeperiod=MA_PERIOD)
    ma = pd.DataFrame({'moving_average': ma})
    ema_val = talib.EMA(df['close'], timeperiod=EMA_PERIOD)
    ema_val = pd.DataFrame({'exponential_moving_average': ema_val})
    return pd.concat([df, ma, ema_val], axis=1).iloc[CUT_BY:]


def is_break_buy(df):
    yesterday_price = df.tail(2).iloc[0]
    is_yesterday_below = yesterday_price['close'] < yesterday_price['moving_average'] or yesterday_price['close'] < \
                         yesterday_price['exponential_moving_average']
    today_price = df.tail(1).iloc[0]
    is_today_up = today_price['close'] > today_price['moving_average'] and today_price['close'] > today_price[
        'exponential_moving_average']
    is_last_sell = is_last_position_sell(df)
    return is_yesterday_below and is_today_up and is_last_sell


def is_last_position_sell(df):
    df_test = df[:-1]
    is_last_sell = False
    for i, row in df_test.iterrows():
        if i == 0: continue
        if row['close'] < row['moving_average'] and row['close'] < row['exponential_moving_average']:
            is_last_sell = True
        if row['close'] > row['moving_average'] and row['close'] > row['exponential_moving_average']:
            is_last_sell = False
    return is_last_sell


def get_action_point(df):
    buy_price = None
    sell_price = None
    action_point = []
    close = df['close']
    ma = df['moving_average']
    ema = df['exponential_moving_average']
    for i in range(1, len(df) - 1, 1):
        is_yesterday_below = close.iloc[i - 1] < ma.iloc[i - 1] and close.iloc[i - 1] < ema.iloc[i - 1]
        is_today_break_up = close.iloc[i] > ma.iloc[i] and close.iloc[i] > ema.iloc[i]
        if is_yesterday_below and is_today_break_up and sell_price is None:
            buy_price = df.iloc[i]['date']

        # is_yesterday_up = close.iloc[i - 1] > ma.iloc[i - 1] or close.iloc[i - 1] > ema.iloc[i - 1]
        is_today_break_down = close.iloc[i] < ma.iloc[i] and close.iloc[i] < ema.iloc[i]
        if is_today_break_down and buy_price is not None:
            sell_price = df.iloc[i]['date']

        if buy_price is not None and sell_price is not None:
            action_point.append(ActionPoint(buy=buy_price, sell=sell_price))
            buy_price = None
            sell_price = None
    return action_point

from datetime import timedelta

MONEY = 1


def get_estimated_profit(df, action_points):
    money = MONEY
    profit = 0
    success = 0
    for ap in action_points:
        price_buy = get_price_action(df, ap.buy)
        price_sell = get_price_action(df, ap.sell)
        stock = money / price_buy
        money = stock * price_sell
        profit = (money - MONEY) / MONEY

        if price_sell > price_buy: success += 1

    hit = 0 if len(action_points) == 0 else (success / len(action_points)) * 100
    return ['{0:.3g}'.format(profit * 100), '{0:.3g}'.format(hit)]


def get_price_action(df, date):
    shifted_buy_time = (date + timedelta(days=1))
    price_buy = df[df['date'] == shifted_buy_time]
    if price_buy.empty:
        return get_price_action(df, shifted_buy_time)
    return (price_buy['open'].item() + price_buy['close'].item()) / 2

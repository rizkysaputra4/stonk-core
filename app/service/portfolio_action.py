from decimal import Decimal

from app.repository.portfolio_repository import save_action, get_total_lot, close_open_position, get_user_portfolio
from app.repository.price_repository import check_if_ticker_exist
from app.service.get_sell_recommentation_service import sell_recommendation


def buy_service(data):
    if data.ticker is None or data.price is None or data.qty is None or data.customer_id is None:
        return "Error: some required element are empty"
    data.ticker = data.ticker.upper()
    if check_if_ticker_exist(data.ticker) == 0:
        return "Error: ticker is invalid"
    save_action(data)
    return "Success"


def sell_service(data):
    if data.ticker is None or data.price is None or data.customer_id is None:
        return "Error: some required element are empty"
    data.ticker = data.ticker.upper()
    if check_if_ticker_exist(data.ticker) == 0:
        return "Error: ticker is invalid"
    total_available_lot = get_total_lot(data)
    data.qty = str(total_available_lot) if data.qty is None else data.qty
    if total_available_lot is None:
        return 'ErrorL: you dont have stock with ticker ' + data.ticker
    if Decimal(data.qty.replace(',','.')) > total_available_lot:
        return 'Error: cant sell more than available lot'

    if str(data.qty) == str(total_available_lot):
        close_open_position(data.ticker)

    save_action(data)
    return 'Success'


def recap_service(data):
    recap = sell_recommendation(data)
    if not recap:
        return "No sell recommendation for today"
    result = "Sell Recommendation: "
    for i, data in enumerate(recap):
        result += f"\n{i + 1}. {data}"
    return result


def get_user_portfolio_service(user_id):
    result = get_user_portfolio(user_id)
    if not result:
        return "Your portfolio is empty"
    out = "Your portfolio"
    for i, v in enumerate(result):
        out += f"\n{i+1}. {v.ticker}, qty: {v.qty}. price: {v.price}"
    return out


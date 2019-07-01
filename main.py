from stock_analyzer_functions import *
from alphavantage import get_api_key


symbol = "AAPL"
data = get_alphavantage_stock_price_daily(symbol, get_api_key())
print(data)

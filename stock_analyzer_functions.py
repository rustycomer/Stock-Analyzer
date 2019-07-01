import pandas as pd
import datetime as dt


def get_sector_holdings(sector_symbol):
    url = "https://www.sectorspdr.com/sectorspdr/IDCO.Client.Spdrs.Holdings/Export/ExportCsv?symbol={}"
    csv_df = pd.read_csv(url.format(sector_symbol), header=1)
    df_to_symbols_list = csv_df[['Symbol']].values.tolist()
    symbols = []
    for sublist in df_to_symbols_list:
        for item in sublist:
            symbols.append(item)
    return symbols


def get_start_date():
    start_date = dt.date.today() - dt.timedelta(days=730)
    return start_date


def get_end_date():
    end_date = dt.date.today()
    return end_date


def get_alphavantage_stock_price_intraday(symbol, api_key, interval=60):
    data = pd.read_json(
        "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={}&interval={}min&apikey={}".format
        (symbol, interval, api_key))
    return data


def get_alphavantage_stock_price_daily(symbol, api_key):
    data = pd.read_json(
        "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&apikey={}".format
        (symbol, api_key))
    return data

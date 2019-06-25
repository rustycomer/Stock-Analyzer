import pandas as pd


def get_sector_holdings(sector_symbol):
    url = "https://www.sectorspdr.com/sectorspdr/IDCO.Client.Spdrs.Holdings/Export/ExportCsv?symbol={}"
    csv_df = pd.read_csv(url.format(sector_symbol), header=1)
    df_to_symbols_list = csv_df[['Symbol']].values.tolist()
    symbols = []
    for sublist in df_to_symbols_list:
        for item in sublist:
            symbols.append(item)
    return symbols


user_input = input("Enter symbol: ")
get_sector_holdings(user_input)

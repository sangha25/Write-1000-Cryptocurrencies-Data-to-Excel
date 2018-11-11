import requests
from openpyxl import Workbook
listings_api = 'https://api.coinmarketcap.com/v2/listings/'
ticker_api = 'https://api.coinmarketcap.com/v2/ticker/?start='
listings_data = requests.get(listings_api).json()['data']

file = Workbook()
sheet = file.create_sheet('Sheet 1',0)
sheet.append(['Name','Symbol','Price','Volume','MarketCap','Change 1h','Change 24h','Change 7d'])


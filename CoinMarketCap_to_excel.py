import requests
from openpyxl import Workbook
listings_api = 'https://api.coinmarketcap.com/v2/listings/'
ticker_api = 'https://api.coinmarketcap.com/v2/ticker/?start='
listings_data = requests.get(listings_api).json()['data']


from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import os
from iexfinance.stocks import Stock
from dotenv import load_dotenv
load_dotenv()

def get_stocks():
    SECRET_KEY = os.getenv("IEX_KEY")
    aapl = Stock("AAPL", token=SECRET_KEY)
    aapl.get_balance_sheet()

get_stocks()

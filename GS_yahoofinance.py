#get historical
import yahoofinance as yf
import pandas_datareader as pdr
import datetime
import sys

#get stock price information for whatever date range needed
#saves to a csv file
#def get_stock_price():
#    while 1:
#        try:
#            symbol = input("=> Enter Stock Symbol (lower case): ")
#            start = input("=> Enter Start Date in YYYY-MM-dirDD format: ")
#            end = input("=> Enter End Date in YYYY-MM-DD format: ")
#            start_year, start_month, start_day = map(int, start.split("-"))
#            end_year, end_month, end_day = map(int, end.split("-"))
#            start_date = datetime.datetime(start_year, start_month, start_day)
#            end_date = datetime.datetime(end_year, end_month, end_day)
#            df = pdr.DataReader(symbol, "yahoo", start_date, end_date)
#            df.to_csv(input("=> Enter File Name to be saved with .csv at the end: "))
#        except KeyboardInterrupt:
#            print("\n=> Keyboard Interrupt! Exiting Program...")
#            sys.exit()
#get_stock_price("AAPL")
print("Hello")
print("2nd verion with Debug")


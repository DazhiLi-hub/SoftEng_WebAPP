from apscheduler.schedulers.blocking import BlockingScheduler
import pandas as pd
import pandas_datareader.data as web
import datetime
import yfinance as yf
def history_data(stock,start):
    start_time = datetime.datetime.strptime(start,"%Y,%m,%d")
    end = datetime.date.today()
    company = web.DataReader(stock, "yahoo", start_time, end)
    print(type(company))
def realtime_data(stock):
    data=yf.download(tickers=stock,period="1d",interval="1m")
    data.head()
    print(data.tail(2))
history_data("AAPL","2016,1,1")
realtime_data("AAPL")
sched=BlockingScheduler()
sched.add_job(realtime_data,'interval',seconds=6,kwargs={"stock":"AAPL"})
sched.start()

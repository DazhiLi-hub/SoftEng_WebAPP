from apscheduler.schedulers.blocking import BlockingScheduler
import pandas as pd
import pandas_datareader.data as web
import datetime
import requests
import re
import json


def history_data(stock, start):
    start_time = datetime.datetime.strptime(start, "%Y,%m,%d")
    end = datetime.date.today()
    company = web.DataReader(stock, "yahoo", start_time, end)
    json_data = company.to_json(orient='table')
    # print(company)
    # print(json_data)
    dir_long = "./" + stock + "_historical_data.json"
    with open(dir_long, "w") as f:
        json.dump(json_data, f)
    print("File Written Successfully...")


def realtime_data():
    url_base = 'https://www.cnbc.com/quotes/?symbol='
    company_name = ["GOOG", "MSFT"]
    for name in company_name:
        url = url_base + name
        strhtml = requests.get(url)
        price = r'<meta itemprop="price" content="(.*?)" />'
        volume = r'"I":{"styles":{"A":""},"values":{"B":"(.*?)"}},"J":'
        timestamp = datetime.datetime.now()
        text_price = re.findall(price, strhtml.text, re.S | re.M)
        text_volume = re.findall(volume, strhtml.text, re.S | re.M)
        '''
        print('The real time price of ' + name + ' is ')
        for m in text_price:
            print(m)
        print('The real time volumn of ' + name + ' is ')
        for m1 in text_volumn:
            print(m1)
        '''
        realtime = {"Time": timestamp,
                    "Price": text_price,
                    "Volumn": text_volume}
        dir_short = "./" + name + "_realtime_data.json"
        with open(dir_short, "a") as f:
            json.dump(realtime, f, indent=4, sort_keys=True, default=str)
            print(name + " File Written Successfully...")


if __name__ == '__main__':
    stocks = ['GOOG', 'MSFT']
    history_data("MSFT","2018,1,1")
    for stock in stocks:
        history_data(stock, "2018,1,1")
    sched = BlockingScheduler()
    sched.add_job(realtime_data, 'interval', minutes=1)
    sched.start()
'''
realtime_data("APPL")
sched = BlockingScheduler()
sched.add_job(realtime_data, 'interval', minutes=1, kwargs={"stock": "AAPL"})
sched.start()
'''


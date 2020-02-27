import pandas_datareader.data as web
import datetime
import json
import re
import requests
from apscheduler.schedulers.blocking import BlockingScheduler
import pymongo

company_name = ["GOOG", "MSFT", "AAPL", "NVDA", "BTC-USD", "AMZN", "OVTZ", "IBM", "AMD", "INTC"]
url_base = 'https://www.cnbc.com/quotes/?symbol='
client = pymongo.MongoClient('localhost')
db = client['stock']


def realtime_data():
    for company in company_name:
        url = url_base + company
        strhtml = requests.get(url)
        price = r'<meta itemprop="price" content="(.*?)" />'
        volume = r'"I":{"styles":{"A":""},"values":{"B":"(.*?)"}},"J":'
        timestamp = datetime.datetime.now()
        text_price = re.findall(price, strhtml.text, re.S | re.M)
        text_volume = re.findall(volume, strhtml.text, re.S | re.M)
        realtime = {"Time": timestamp,
                    "Price": text_price,
                    "Volumn": text_volume}
        collection1 = db[company + '_realtime_data']
        db.drop_collection(collection1)
        collection1.insert(realtime)
        dir_short = "/Users/lucifer.w/Documents/568/project/phase1/data/" + company + "_realtime_data.json"
        with open(dir_short, "a") as f:
            json.dump(realtime, f, indent=4, sort_keys=True, default=str)
            print(company + " Realtime  File Written Successfully...")


def history_data(stock, start):
    start_time = datetime.datetime.strptime(start, "%Y,%m,%d")
    end = datetime.date.today()
    company = web.DataReader(stock, "yahoo", start_time, end)
    time = []
    for i in company.index:
        time.append(datetime.datetime.strftime(i, "%Y-%m-%d"))
    company['index'] = time
    company['Time'] = time
    dict = company.set_index('index').T.to_dict('dict')

    # print(type(json_data))
    return dict

    # dir_long = "/Users/lucifer.w/Documents/568/project/phase1/data/" + stock + "_historical_data.json"
    # with open(dir_long, "w") as f:
    #     json.dump(json_data, f)
    # print(stock + " History File Written Successfully...")
    # return dir_long


if __name__ == '__main__':
    for name in company_name:
        output = []
        his = history_data(name, "2019,1,1")
        # history_data(name, "2019,1,1")
        # Collect historical time in a json file
        collection = db[name + '_historical_data']
        db.drop_collection(collection)
        # Clear the data that is stored in the database last time
        for day in his:
            collection.insert(his[day])
        for i in collection.find():
            i['_id'] = re.findall("'(.*)'", i.get('_id').__repr__())[0]
            output.append(i)
        with open('/Users/lucifer.w/Documents/568/project/phase1/data/' + name + '.json', 'w', encoding="UTF-8") as jf:
            jf.write(json.dumps(output, indent=2))
    sched = BlockingScheduler()
    sched.add_job(realtime_data, 'interval', minutes=1, next_run_time=datetime.datetime.now())
    sched.start()

# SoftEng_WebAPP
**This is a Team Project for Contributors: SifanYuan, Haocong Wang, Mingming Pei, Dazhi Li**

## Phase I: Data Collecting

### First Period Target:
- Collecting data from Yahoo Finance
- Stocks included:GOOG(Google), MSFT(Microsoft),AAPL(Apple),NVDA(NVDIA),BTC-USD(Bitcoin),AMZN(Amazon),OVTZ(Oclus Vison Tech.),IBM(IBM),AMD(AMD),INTC(Intel)
- Utilized language: Python
- Database: MongoDB(Non-relation)
- Data transfered datatype: .json
- Data are divided into 2 parts: History data(2017-1-1 to Now), Realtime data(One day stock price&volome per minute)
- Runing Final_collector.py to enter, continuously fetching real-time data until keyborad interrupt(Ctrl + C)

### Requierement:
- apscheduler
- pandas
- pandas-datareader
- datetime
- requests
- re
- json

### Runing Result:

## References:
[实例操作：Python提取雅虎财经数据及可视化分析](https://blog.csdn.net/Hellolijunshy/article/details/82527643)

[Stock Market Data and Analysis in Python](https://blog.quantinsti.com/stock-market-data-analysis-python/)

[pandas.DataFrame.to_json按行转json](https://blog.csdn.net/huanbia/article/details/72674832)

[Python 定时任务的实现方式](https://lz5z.com/Python%E5%AE%9A%E6%97%B6%E4%BB%BB%E5%8A%A1%E7%9A%84%E5%AE%9E%E7%8E%B0%E6%96%B9%E5%BC%8F/)

[apscheduler如何传递参数给job](https://blog.csdn.net/wyongqing/article/details/46738405)

[python读写json文件](https://www.cnblogs.com/bigberg/p/6430095.html)

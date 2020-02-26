import requests
import re

url_base = 'https://www.cnbc.com/quotes/?symbol='
company_name=["GOOG","AAPL"]
for name in company_name:
    url=url_base+name
    strhtml = requests.get(url)
    price = r'<meta itemprop="price" content="(.*?)" />'
    volumn = r'"I":{"styles":{"A":""},"values":{"B":"(.*?)"}},"J":'
    # <span class="last original ng-binding" ng-bind="quoteData['AAPL'].lastOutputoriginal | filter:processStripCondition('AAPL','last','original')">292.70</span>
    # <meta itemprop="price" content="292.76" />
    # "I":{"styles":{"A":""},"values":{"B":"43,559,361"}},"J":
    text_price = re.findall(price, strhtml.text, re.S | re.M)
    # print(strhtml.text)
    print('The real time price of '+name+' is ')
    for m in text_price:
        print(m)

    text_volumn = re.findall(volumn, strhtml.text, re.S | re.M)
    # print(strhtml.text)
    print('The real time volumn of '+name+' is ')
    for m1 in text_volumn:
        print(m1)

# strhtml = requests.get(url)
# price = r'<meta itemprop="price" content="(.*?)" />'
# volumn =r'"I":{"styles":{"A":""},"values":{"B":"(.*?)"}},"J":'
# #<span class="last original ng-binding" ng-bind="quoteData['AAPL'].lastOutputoriginal | filter:processStripCondition('AAPL','last','original')">292.70</span>
# #<meta itemprop="price" content="292.76" />
# #"I":{"styles":{"A":""},"values":{"B":"43,559,361"}},"J":
# text_price = re.findall(price, strhtml.text, re.S|re.M)
# #print(strhtml.text)
# print('The real time price is ')
# for m in text_price:
#     print (m)
#
# text_volumn = re.findall(volumn, strhtml.text, re.S|re.M)
# #print(strhtml.text)
# print('The real time volumn is ')
# for m1 in text_volumn:
#     print (m1)
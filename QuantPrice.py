# -*- coding: utf-8 -*-



import requests
import bs4
import pandas as pd
import time

def make_price_dataframe(code, timeframe, count):
    url = 'https://fchart.stock.naver.com/sise.nhn?requestType=0'
    price_url = url + '&symbol=' + code + '&timeframe=' + timeframe + '&count=' + count
    
    price_data = requests.get(price_url)
    price_data_bs = bs4.BeautifulSoup(price_data.text, 'lxml')
    item_list = price_data_bs.findAll('item')
    
    date_list = []
    price_list = []

    for item in item_list:
        temp_data = item['data']
        datas = temp_data.split('|')
        date_list.append(datas[0])
        price_list.append(datas[4])
    
    price_df = pd.DataFrame({code:price_list}, index=date_list)
    
    return price_df

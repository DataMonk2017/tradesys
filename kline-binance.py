# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 21:08:28 2018

@author: jianyuan
"""

import time
from binance.websockets import BinanceSocketManager
from binance.enums import *
from binance.client import Client
from tradesys import save_data
#API Key:
#Secret:
api_key = 'hjdDOjx7Lu8fU2dFS2YBVYUPYJylqAPbdPkcQp9jQFqV0h8ZZswtxdmXGALyc0RH' 
api_secret = 'GcWPwwPd5uz6wqxyNgMvxt2WHFbAvkjyeGLy6xVso5ToIERC56tLXRRgk4u98DZz'
proxies = {
    'http': 'http://127.0.0.1:1080',
    'https': 'https://127.0.0.1:1080'
}
client = Client(api_key, api_secret,{'proxies': proxies})
client.ping()

#client.get_system_status()
#%%
#client.get_products()
#%%
bm = BinanceSocketManager(client)
def process_message(msg):
    print("message type: {}".format(msg['e']))
    print(msg)
#%%
#conn_key = bm.start_kline_socket('BNBBTC', process_message, interval=KLINE_INTERVAL_1MINUTE)
#bm.start()
#int(time.time()*1000)
#from datetime import datetime
#datetime.fromtimestamp(1522649399999/1000)
#%%
while 1:    
    candles = client.get_klines(symbol='BNBBTC', interval=Client.KLINE_INTERVAL_1MINUTE)
    save_data(candles)
    #print(candles[-1])
    time.sleep(2)
    
#%%
#candles = client.get_klines(symbol='BNBBTC', interval=Client.KLINE_INTERVAL_5MINUTE, startTime=,endTime=)
 
#candles1 = client.get_klines(symbol='BNBBTC', interval=Client.KLINE_INTERVAL_5MINUTE)

#bm.close()
#%%
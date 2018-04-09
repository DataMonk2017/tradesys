# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 21:08:28 2018

@author: jianyuan
"""

#%%
import requests
import time
from tradesys import save_data
def using_requests(request_url, apisign):
    http_proxy  = "http://127.0.0.1:1080"
    https_proxy = "https://127.0.0.1:1080"
    ftp_proxy   = "ftp://127.0.0.1:1080"
    
    proxyDict = { 
                  "http"  : http_proxy, 
                  "https" : https_proxy, 
                  "ftp"   : ftp_proxy
                }
    return requests.get(
        request_url,
        headers={"apisign": apisign},
        proxies=proxyDict,
        timeout=10
    ).json()
    
from bittrex.bittrex import Bittrex, API_V2_0
my_bittrex = Bittrex(None, None, dispatch=using_requests, api_version=API_V2_0)  # or defaulting to v1.1 as Bittrex(None, None)

first = 'BTC'
last = 'ETH'

symbol = ''.join(first,'-',last)


while 1:
    result=my_bittrex.get_candles(symbol,"oneMin")
    save_data(result[-1])
    time.sleep(2)
    
"""
TICKINTERVAL_ONEMIN = 'oneMin'
TICKINTERVAL_FIVEMIN = 'fiveMin'
TICKINTERVAL_HOUR = 'hour'
TICKINTERVAL_THIRTYMIN = 'thirtyMin'
TICKINTERVAL_DAY = 'Day'
"""
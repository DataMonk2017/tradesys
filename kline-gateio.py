# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 21:08:28 2018

@author: jianyuan
"""

#%%
from bittrex.bittrex import Bittrex, API_V2_0
my_bittrex = Bittrex(None, None, api_version=API_V2_0)  # or defaulting to v1.1 as Bittrex(None, None)
my_bittrex.get_candles("BTC-ETH","oneMin")
"""
TICKINTERVAL_ONEMIN = 'oneMin'
TICKINTERVAL_FIVEMIN = 'fiveMin'
TICKINTERVAL_HOUR = 'hour'
TICKINTERVAL_THIRTYMIN = 'thirtyMin'
TICKINTERVAL_DAY = 'Day'
"""
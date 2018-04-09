# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 21:08:28 2018

@author: jianyuan
"""

#%%
import gdax
public_client = gdax.PublicClient()
public_client.get_product_ticker(product_id='ETH-USD')
#%%
public_client.get_products()
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 17:10:20 2018

@author: jianyuan
"""
from websocket import create_connection
import gzip
import time
from tradesys import save_data
def get_request_str(first,last,p_id,action='req',detail="kline"):
    symbol = first+last
    if detail == 'kline':
            #到时候限制时间 from,to 其他的东西
        ret = """{"%s": "market.%s.kline.1min", "id": "%s"}"""%(action,symbol,p_id)
    elif detail == "marketdetail":
        ret = """{"%s": "market.%s.detail", "id": "%s"}"""%(action,symbol,p_id)
    elif detail == "marketdepth":
        ret = """{"%s": "market.%s.depth.step5", "id": "%s"}"""%(action,symbol,p_id) 
    elif detail == "tradedetail":
        ret = """{"%s": "market.%s.trade.detail", "id": "%s"}"""%(action,symbol,p_id)        
    return ret

#def get_kline():    
    
def huobi(first,last,p_id,action,detail):
    while(1):
        try:
            ws = create_connection("wss://api.huobipro.com/ws")
            break
        except:
            print('connect ws error,retry...')
            time.sleep(5)

    
    tradeStr = get_request_str(first,last,p_id,action,detail)

    ws.send(tradeStr)
    while(1):
        compressData=ws.recv()
        result=gzip.decompress(compressData).decode('utf-8')
        if result[:7] == '{"ping"':
            ts=result[8:21]
            pong='{"pong":'+ts+'}'
            ws.send(pong)
            ws.send(tradeStr)
        else:
            save_data(result)
    
detail = "kline"        
action = "req" #req/sub
first ='eth'
last = 'btc'
p_id = "id12"
huobi(first,last,p_id,action,detail)    
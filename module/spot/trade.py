import pandas as pd
import requests
import math
from typing import List, Optional
from module.spot import market

def batch_orders(USER_KEY: str, symbol: Optional[str], batchMode: str, orderList: List) -> pd.DataFrame:
    for order in orderList:
        symbol = order['symbol']
        res = market.symbol_info(USER_KEY, symbol)
        if order['side'] == 'buy':        
            decimal = int(res['quotePrecision'])
        elif order['side'] == 'sell':
            decimal = int(res['quantityPrecision'])
        
        order["size"] = str(math.floor(float(order['size']) * 10**decimal) / 10**decimal)

    url = "https://bitgettrader.fin.cloud.ainode.ai/spot/trade/batch-orders"
        
    headers = {
        "API-KEY": USER_KEY,
        "Target-Email": None
    }
    
    json = {
        "symbol": symbol,
        "batchMode": batchMode,
        "orderList": orderList,
    }
    
    res = requests.post(url, json=json, headers=headers)
    data = response.json()['data']
    
    rows = []
    # 성공 리스트 처리
    for item in data.get('successList', []):
        orderId = item.get('orderId', '')
        clientOid = item.get('clientOid', '')
        result = "success"
        rows.append([orderId, clientOid, result, "", ""])
    
    # 실패 리스트 처리
    for item in data.get('failureList', []):
        orderId = item.get('orderId', '')
        clientOid = item.get('clientOid', '')
        result = "failure"
        errorMsg = item.get('errorMsg', '')
        errorCode = item.get('errorCode', '')
        rows.append([orderId, clientOid, result, errorMsg, errorCode])
        
    df = pd.DataFrame(rows, columns=["orderId", "clientOid", "result", "errorMsg", "errorCode"])
    return df

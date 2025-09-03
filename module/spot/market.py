import pandas as pd
import requests

def symbol_info(USER_KEY: str, symbol: str) -> pd.DataFrame:
    url = "https://bitgettrader.fin.cloud.ainode.ai/spot/market/symbol-info"
    headers = {
        "API-KEY": user_key,
        "Target-Email": None
    }
  
    json = {
        "symbol": symbol
    }

    res = request.post(url, json=json, headers=headers) 
    data = res.json()['data']
    df = pd.DataFrame(data)
    return df

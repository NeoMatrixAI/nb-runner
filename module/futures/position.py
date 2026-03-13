import pandas as pd
import requests

def all_positions(USER_KEY: str, paptrading: str, productType: str, marginCoin: str) -> pd.DataFrame:
    if paptrading == 'live':
        url = "https://bitgettrader.fin.cloud.ainode.ai/futures/position/all-positions"
    elif paptrading == 'demo':
        url = "https://bitgettrader.fin.cloud.ainode.ai/demo/futures/position/all-positions"
    else:
        print(f"Error: Trading Method '{paptrading}' does not exist")
        raise ValueError(status_code=400, detail=f"Trading Method '{paptrading}' is not supported. Please enter 'live' or 'demo'.")
      
    headers = {
        "API-KEY": USER_KEY,
        "Target-Email": None
    }

    json = {
        "productType": productType,
        'marginCoin': marginCoin.upper()
    }

    response = requests.post(url, json=json, headers=headers)
    
    try:
        data = response.json()['data']
        df = pd.DataFrame(data)
        return df
    except:
        print("There is no position")
        return pd.DataFrame()
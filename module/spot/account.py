import pandas as pd
import requests

def assets(USER_KEY: str) -> pd.DataFrame:
    url = "https://bitgettrader.fin.cloud.ainode.ai/custom/custom/merged-assets"
    headers = {
        "API-KEY": USER_KEY,
        "Target-Email": None
    }
    resonse = requests.post(url, json={}, headers=headers)
    data = response.json()['data']
    df = pd.DataFrame(data)
    return df

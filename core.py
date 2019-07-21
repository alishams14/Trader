# coding: utf-8

# In[9]:


import json
import requests
import time

import trend

# api_key = str(input("API key: "))
# secret_key = str(input("Secret key: "))
# symbol = str(input("Symbol: "))

api_key = ""
secret_key = ""
symbol = ""


# In[2]:

api_url = json.loads(open("api_url.json").read())
order_url = api_url["trading"]["order"]["url"]


def request(side, url, data=None):
    """Send out the requests"""

    session = requests.Session()
    response = session.request(side, url, data=data, auth=(api_key, secret_key))

    if response.status_code != 200:
        err_message = response.json()["error"]["message"]
        return err_message

    return response.json()


def get_candle(period):
    url = api_url["public"]["candles"]["url"] % (symbol, period)
    return request("GET", url)


# In[6]:


def upword_ema_5():
    candles_5 = get_candle("M5")

    if float(trend.ema_indicator(candles_5, 14)[97]) < float(
        trend.ema_indicator(candles_5, 40)[97]
    ) and float(trend.ema_indicator(candles_5, 14)[98]) > float(
        trend.ema_indicator(candles_5, 40)[98]
    ):
        return "A"


def upword_ema_15():
    candles_15 = get_candle("M15")

    if float(trend.ema_indicator(candles_15, 14)[97]) < float(
        trend.ema_indicator(candles_15, 40)[97]
    ) and float(trend.ema_indicator(candles_15, 14)[98]) > float(
        trend.ema_indicator(candles_15, 40)[98]
    ):
        return "C"


def upword_ema_60():
    candles_h1 = get_candle("H1")

    if float(trend.ema_indicator(candles_h1, 14)[97]) < float(
        trend.ema_indicator(candles_h1, 40)[97]
    ) and float(trend.ema_indicator(candles_h1, 14)[98]) > float(
        trend.ema_indicator(candles_h1, 40)[98]
    ):
        return "C"


def upword_ema_240():
    candles_h4 = get_candle("H4")

    if float(trend.ema_indicator(candles_h4, 14)[97]) < float(
        trend.ema_indicator(candles_h4, 40)[97]
    ) and float(trend.ema_indicator(candles_h4, 14)[98]) > float(
        trend.ema_indicator(candles_h4, 40)[98]
    ):
        return "C"


def downword_ema_5():
    candles_5 = get_candle("M5")

    if float(trend.ema_indicator(candles_5, 14)[97]) > float(
        trend.ema_indicator(candles_5, 40)[97]
    ) and float(trend.ema_indicator(candles_5, 14)[98]) < float(
        trend.ema_indicator(candles_5, 40)[98]
    ):
        return "B"

def downword_ema_15():
    candles_15 = get_candle("M15")

    if float(trend.ema_indicator(candles_15, 14)[97]) > float(
        trend.ema_indicator(candles_15, 40)[97]
    ) and float(trend.ema_indicator(candles_15, 14)[98]) < float(
        trend.ema_indicator(candles_15, 40)[98]
    ):
        return "C"

# In[7]:


def buy_logic():
    if upword_ema_5():
        return True

    elif upword_ema_15():
        return True

    elif upword_ema_60():
        return True
    
    elif upword_ema_240():
        return True

def sell_logic():
    candles_15 = get_candle("M15")
    candles_h1 = get_candle("H1")
    candles_h4 = get_candle("H4")
    last_close = float(candles_15[98]["close"]) * 0.99
    buy_price = 1

    if last_close > 1.0069 * buy_price and \
        float(trend.ema_indicator(candles_15, 14)[98]) < float(trend.ema_indicator(candles_15, 40)[98]):
        return True
    
    elif last_close > 1.01213 * buy_price and \
        float(trend.ema_indicator(candles_h1, 14)[98]) < float(trend.ema_indicator(candles_h1, 40)[98]):
        return True

    elif last_close > 1.0213 * buy_price and \
        float(trend.ema_indicator(candles_h4, 14)[98]) < float(trend.ema_indicator(candles_h4, 40)[98]):
        return True
    
    elif downword_ema_5():
        return True
    
    elif downword_ema_15():
        return True
    
# In[10]:

while True:
    if buy_logic():
        candles_5 = get_candle("M5")
        last_close = float(candles_5[98]["close"]) * 0.99
        response = requests.get('https://api.hitbtc.com/api/2/trading/balance',
                        auth=(api_key, secret_key))
        quantity = 0
        for i in response.json():
            if i['currency'] == 'USD':
                if float(i['available']) > 10:
                    quantity = i['available']
        
        data = {
            "symbol": symbol,
            "side": "buy",
            "quantity": quantity,
            "price": last_close,
        }
        url = api_url["trading"]["order"]["url"]
        result = request("POST", url, data)
        print("\033[33m%s\033[0m" % result.json())
    else:
        print("\033[31mStrategy failed!\033[0m")
    time.sleep(10)

# In[ ]:

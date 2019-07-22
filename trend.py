# coding: utf-8

# In[7]:


import ta
import util


# In[11]:


def ao(candles, short_window, long_window, fillna=False):
    """Awesome Oscillator"""

    highs = util.filtership(candles, "max")
    lows = util.filtership(candles, "min")
    result = ta.ao(highs, lows, short_window, long_window, fillna)

    return result


def money_flow_index(candles, window, fillna=False):
    """Money Flow Index"""

    highs = util.filtership(candles, "max")
    lows = util.filtership(candles, "min")
    closes = util.filtership(candles, "close")
    volumes = util.filtership(candles, "volume")
    result = ta.money_flow_index(highs, lows, closes, volumes, window, fillna)

    return result


def rsi(candles, window, fillna=False):
    """Relative Strength Index"""

    closes = util.filtership(candles, "close")
    result = ta.rsi(closes, window, fillna)

    return result


def stoch(candles, window, fillna=False):
    """Stochastic Oscillator"""

    highs = util.filtership(candles, "max")
    lows = util.filtership(candles, "min")
    closes = util.filtership(candles, "close")
    result = ta.stoch(highs, lows, closes, window, fillna)

    return result


def tsi(candles, high_window, low_window, fillna=False):
    """True strength Index"""

    closes = util.filtership(candles, "close")
    result = ta.tsi(closes, high_window, low_window, fillna)

    return result


def ema_indicator(candles, window):

    closes = util.filtership(candles, "close")
    result = ta.ema_indicator(closes, window)

    return result


# In[ ]:

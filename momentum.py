# coding: utf-8

# In[9]:


import ta
import util


# In[10]:


def ao(candles, short_window, long_window):
    """Awesome Oscillator"""

    highs = util.filtership(candles, "max")
    lows = util.filtership(candles, "min")
    result = ta.ao(highs, lows, short_window, long_window)

    return result


def money_flow_index(candles, window):
    """Money Flow Index"""

    highs = util.filtership(candles, "max")
    lows = util.filtership(candles, "min")
    closes = util.filtership(candles, "close")
    volumes = util.filtership(candles, "volume")
    result = ta.money_flow_index(highs, lows, closes, volumes, window)

    return result


def rsi(candles, window):
    """Relative Strength Index"""

    closes = util.filtership(candles, "close")
    result = ta.rsi(closes, window)

    return result


def stoch(candles, window):
    """Stochastic Oscillator"""

    highs = util.filtership(candles, "max")
    lows = util.filtership(candles, "min")
    closes = util.filtership(candles, "close")
    result = ta.stoch(highs, lows, closes, window)

    return result


def tsi(candles, high_window, low_window):
    """True strength Index"""

    closes = util.filtership(candles, "close")
    result = ta.tsi(closes, high_window, low_window)

    return result


# In[ ]:

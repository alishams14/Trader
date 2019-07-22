# coding: utf-8

# In[3]:


import pandas as pd

# In[4]:


def filtership(candles, fetch, reverse=None):
    """Fetch the requested value from candles"""

    values = [
        float(candles[i][fetch]) for i in range(0, len(candles) - 1)
    ]  # Not get current candle
    if reverse:
        values.reverse()
    df = pd.Series(values)
    return df


# In[ ]:

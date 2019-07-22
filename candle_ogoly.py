import requests
import util

session = requests.session()


def get(url):
    response = session.get(url)
    return response.json()


state = ""
candles = get("https://api.hitbtc.com/api/2/public/candles/ETHUSD")
close = float(util.filtership(candles, "close")[98])
_open = float(util.filtership(candles, "open")[98])
low = float(util.filtership(candles, "min")[98])
high = float(util.filtership(candles, "max")[98])

if close - _open > 0:
    state = "HPlus"

if close - _open < 0.5 * (_open - low) and close - _open > 1.1 * (high - close):
    state = "Doji"

if close - _open < 0.25 * (high - close) and close - _open < 0.5 * (_open - low):
    state = "Doji"

if close - _open < 0.5 * (high - close) and close - _open > 1.1 * (_open - low):
    state = "DHPlus"

if close - _open < 0:
    state = "HNeg"

if _open - close < 0.5 * (close - low) and _open - close > 1.1 * (high - _open):
    state = "DojiNeg"

if _open - close < 0.25 * (high - _open) and _open - close < 0.5 * (close - low):
    state = "DojiNeg"

if _open - close < 0.5 * (high - _open) and _open - close > 1.1 * (close - low):
    state = "DHNeg"

print(state)

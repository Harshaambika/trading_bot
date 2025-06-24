import streamlit as st
import pandas as pd
from binance_client import get_binance_client
from rsi_strategy import calculate_rsi
from trade_bot import place_market_order

client = get_binance_client()
symbol = "BTCUSDT"
quantity = 0.001

st.title("📈 RSI Auto-Trader Bot")
st.write("Using Binance Futures Testnet")

# Fetch historical klines
klines = client.futures_klines(symbol=symbol, interval='1m', limit=100)
df = pd.DataFrame(klines, columns=['time','open','high','low','close','volume','close_time',
                                   'quote_asset_volume','num_trades','taker_buy_base',
                                   'taker_buy_quote','ignore'])
df['close'] = df['close'].astype(float)

# Calculate RSI
df['RSI'] = calculate_rsi(df['close'])

# Display latest RSI and decision
latest_rsi = df['RSI'].iloc[-1]
latest_price = df['close'].iloc[-1]

st.metric("Latest Price", f"${latest_price:.2f}")
st.metric("RSI (14)", f"{latest_rsi:.2f}")

# Decision logic
signal = "HOLD"
if latest_rsi < 30:
    signal = "BUY"
elif latest_rsi > 70:
    signal = "SELL"

st.subheader(f"Signal: 🚨 {signal}")

# Manual Trade Buttons
if st.button("Place BUY Order"):
    order = place_market_order(symbol, "BUY", quantity)
    st.success(f"BUY order placed: {order}")

if st.button("Place SELL Order"):
    order = place_market_order(symbol, "SELL", quantity)
    st.success(f"SELL order placed: {order}")

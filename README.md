# RSI Auto-Trading Bot (Binance Testnet)

## Features
- Uses RSI(14) strategy to place trades
- Fetches live data from Binance Futures Testnet
- Streamlit UI to monitor and place trades
- Python-Binance API with logging and error handling

## How to Run
1. Replace your `API_KEY` and `API_SECRET` in `config.py`
2. Install dependencies:
   ```
   pip install streamlit python-binance pandas
   ```
3. Run the app:
   ```
   streamlit run streamlit_app.py
   ```

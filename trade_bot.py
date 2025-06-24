from binance.exceptions import BinanceAPIException
from logger import setup_logger
from binance_client import get_binance_client

logger = setup_logger()
client = get_binance_client()

def place_market_order(symbol, side, quantity):
    try:
        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type='MARKET',
            quantity=quantity
        )
        logger.info(f"Market order placed: {response}")
        return response
    except BinanceAPIException as e:
        logger.error(f"API Error: {e.message}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return None

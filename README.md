# Crypto Trading Bot

This is a simple crypto trading bot built with Python using the Binance Spot Testnet API. It allows placing MARKET and LIMIT orders from the command line.

 #Features
- Supports BUY and SELL orders
- Allows MARKET and LIMIT order types
- Uses Binance Spot Testnet (no real money)
  
#How to Run
```bash
pip install python-binance
python Trading_Bot.py

#Example input
Enter pair (e.g., BTCUSDT): BTCUSDT
BUY or SELL: BUY
Enter order type (MARKET / LIMIT): LIMIT
Quantity: 0.001
Enter limit price: 63000


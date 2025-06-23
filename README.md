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
Enter pair: BTCUSDT
BUY or SELL: BUY
Order type: LIMIT
Quantity: 0.001
Limit price: 63000
Enter limit price: 63000
Order placed successfully!
Order ID: 123456789 | Status: NEW



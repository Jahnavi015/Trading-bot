from binance.client import Client

api_key = '5gxS3PZu7IA1b4UWRuFI210FTmi8gK7Yv3lW8SlHhqePeeAPoT8Wy0qnOEFCvLza'
api_secret = 'WQADP7ckBKBuFnFWfvUSttEBSbhsXn3yy2oU461q35ghF2pOJ9AngAqYIsKRGtBw'
client = Client(api_key, api_secret)
client.API_URL = 'https://testnet.binance.vision/api' 

symbol = input("Enter pair (e.g., BTCUSDT): ").upper()
side = input("BUY or SELL: ").upper()
order_type = input("Enter order type (MARKET / LIMIT): ").upper()
quantity = float(input("Quantity: "))

try:
    if order_type == 'MARKET':
        order = client.create_order(
            symbol=symbol,
            side=side,
            type='MARKET',
            quantity=quantity
        )
    elif order_type == 'LIMIT':
        price = input("Enter limit price: ")
        order = client.create_order(
            symbol=symbol,
            side=side,
            type='LIMIT',
            quantity=quantity,
            price=price,
            timeInForce='GTC'
        )
    print("Order placed!")
    print("Order ID:", order['orderId'], "| Status:", order['status'])

except Exception as e:
    print("Error placing order:", e)

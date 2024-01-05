import requests

host = "https://api.gateio.ws"
prefix = "/api/v4"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

# Get Spot data
spot_url = '/spot/tickers'
spot_response = requests.get(host + prefix + spot_url, headers=headers)
spot_data = spot_response.json()

# Get Futures data
futures_url = '/futures/usdt/contracts'
futures_response = requests.get(host + prefix + futures_url, headers=headers)
futures_data = futures_response.json()

# Create a dictionary to store the last prices for each currency pair
spot_prices = {ticker['currency_pair']: float(ticker['last']) for ticker in spot_data}
futures_prices = {contract['name']: float(contract['last_price']) for contract in futures_data}

# Find common currency pairs between Spot and Futures
common_pairs = set(spot_prices.keys()) & set(futures_prices.keys())

# Print the results
print("Currency Pair\t\t\tSpot Last\t\t\tFutures Last\t\t\tDifference (Spot - Futures)")
for pair in common_pairs:
    spot_last = spot_prices.get(pair, 0)
    futures_last = futures_prices.get(pair, 0)
    diff = spot_last - futures_last
    print(f"{pair}\t\t\t{spot_last}\t\t\t{futures_last}\t\t\t{diff}")

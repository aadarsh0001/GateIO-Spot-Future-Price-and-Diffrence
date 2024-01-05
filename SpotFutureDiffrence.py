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

# Calculate the difference in last prices
differences = {pair: spot_prices[pair] - futures_prices[pair] for pair in common_pairs}

# Sort differences from maximum to minimum
sorted_differences = dict(sorted(differences.items(), key=lambda item: item[1], reverse=True))

# Print the results
print("Currency Pair\t\tDifference (Spot - Futures)")
for pair, diff in sorted_differences.items():
    print(f"{pair}\t\t\t{diff}")

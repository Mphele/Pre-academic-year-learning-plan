import requests
import sys
while True:
    try:
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=INSERT KEY HERE TO TEST")
        break
    except requests.RequestException:
        print("API error")
        sys.exit()

content = response.json()
data = content['data']
bitcoin_price = float(data['priceUsd'])
try:
    if len(sys.argv)<2:
        print("Missing command-line argument")
        sys.exit(1)
    total_price = float(sys.argv[1])*bitcoin_price
    print(f"${total_price:,.4f}:")
except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)

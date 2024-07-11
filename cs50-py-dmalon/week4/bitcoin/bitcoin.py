# .venvvishnuparandhaman@Vishnus-MacBook-Air-2 bitcoin % python bitcoin.py 10

import requests
import json
import sys

def main():

    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)

    try:

        amount = float(sys.argv[1])
        if amount <= 0:
             print("Amount must be greater than zero.")
             sys.exit(1)

        conversion_rate = get_bitcoin_rate()

        bitcoin_purchase_price = conversion_rate * amount
        formatted_value = "{:,.4f}".format(bitcoin_purchase_price)
        print(f"Rate: ${formatted_value}")

    except requests.RequestException:
        print("Someting is wrong!")
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)

def get_bitcoin_rate():
    # change the limit
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    json_value = response.json()

    # print(json.dumps(json_value, indent=2))

    # Accessing the "code" and "rate" for USD
    usd_code = json_value['bpi']['USD']['code']
    rate_float = json_value['bpi']['USD']['rate_float']

    return rate_float
       
if __name__ == "__main__":
    main()

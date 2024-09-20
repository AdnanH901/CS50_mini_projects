import sys
import requests


def main():
    try:
        n = float(sys.argv[1])
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        bitcoin_list = r.json()
        bitcoin_USD = bitcoin_list["bpi"]["USD"]["rate_float"]
        amount = bitcoin_USD * n
        print(f"${amount:,.4f}")
    except IndexError:
         sys.exit("Missing command-line argument")
    except ValueError:
         sys.exit("Command-line argument is not a number")
    except requests.RequestException:
        print("request error")


if __name__ == "__main__":
    main()

# python bitcoin.py

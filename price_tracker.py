import requests

def get_crypto_price(coin_id='bitcoin'):
    """
    Fetches the current price of a cryptocurrency using CoinGecko's API.
    :param coin_id: The CoinGecko ID of the cryptocurrency (default: bitcoin).
    :return: The current price in USD.
    """
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd'
    response = requests.get(url)
    price = response.json()[coin_id]['usd']
    return price

def main():
    coin_id = input("Enter the CoinGecko ID of the cryptocurrency (e.g., 'bitcoin', 'ethereum'): ").lower().strip()
    try:
        price = get_crypto_price(coin_id)
        print(f"The current price of {coin_id} is: ${price}")
    except Exception as e:
        print(f"Error fetching price for {coin_id}: {e}")

if __name__ == '__main__':
    main()

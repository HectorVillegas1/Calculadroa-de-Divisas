import requests # type: ignore

class ExchangeRateAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

    def get_exchange_rate(self, from_currency, to_currency):
        response = requests.get(self.url + from_currency)
        if response.status_code == 200:
            data = response.json()
            rates = data['conversion_rates']
            return rates.get(to_currency, None)
        else:
            print(f"Error: {response.json().get('error-type')}")
            return None

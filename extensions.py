import json
import requests
from config import keys

class ConvertionException(Exception):
    pass

class APIException:
    @staticmethod
    def convert(quote: str, base: str, amount: float):
        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество')

        url = f'https://api.apilayer.com/currency_data/convert?to={base_ticker}&from={quote_ticker}&amount=1'

        payload = {}
        headers = {
            "apikey": "fGEcFBVV5EPoaoCClWv31TAYOoydVYHL"
        }

        response = requests.request("GET", url, headers=headers, data=payload).json()

        total_base = response['result']*amount


        return total_base
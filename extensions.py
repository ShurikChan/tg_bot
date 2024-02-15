import requests
import json
from config import keys, HEADERS



class APIException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise APIException("Невозможно перевести одинаковые валюты")
        
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f"Не удалось обработать валюту {quote}")
        
        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f"Не удалось обработать валюту {base}")
        
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f"Неверное количество {amount}")
        
        r = requests.get(f'https://api.apilayer.com/exchangerates_data/convert?to={base_ticker}&from={quote_ticker}&amount={amount}', headers=HEADERS)
        total_base = round(json.loads(r.content)['result'], 2)
        return total_base
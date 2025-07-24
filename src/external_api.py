import os

import requests
from dotenv import load_dotenv


def amount_transaction(transaction: dict) -> float:
    """Функция возвращает сумму транзакций в рублях"""
    code_transaction = transaction["operationAmount"]["currency"]["code"]
    amount_transaction = transaction["operationAmount"]["amount"]
    if code_transaction == "RUB":
        return float(amount_transaction)
    else:
        load_dotenv(".env")
        API_KEY = os.getenv("API_KEY")
        headers = {"apikey": API_KEY}

        response = requests.get(
            f"https://api.apilayer.com/exchangerates_data/convert?"
            f"to={"RUB"}&from={code_transaction}&amount={amount_transaction}",
            headers=headers,
        )
        return float(round(response.json()["result"], 2))

import requests


def amount_transactions(transactions: dict) -> float:
    ''' Функция возвращает сумму транзакций в рублях '''
    code_transaction = transactions["operationAmount"]["currency"]["code"]
    amount_transaction = transactions["operationAmount"]["amount"]
    headers = {
        "apikey": "oUrDT4eY1UzK6oyowMSZRcQNcsAYoJ4o"
    }
    if code_transaction == "RUB":
        return float(amount_transaction)
    else:
        response = requests.get(
            f"https://api.apilayer.com/exchangerates_data/convert?to={"RUB"}&from={code_transaction}&amount={amount_transaction}",
            headers=headers)
        # response.json()
        return round(float(response.json()['result']), 2)

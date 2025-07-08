def filter_by_currency(transactions: list, currency_code: str = '') -> str:
    """Функция принимает на вход список словарей, представляющих транзакции.
    Возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной."""
    if currency_code == '':
        yield transactions
    else:
        for transaction in transactions:
            if transaction["operationAmount"]["currency"]["code"] == currency_code:
                yield transaction


def transaction_descriptions(transactions: list) -> str:
    """Принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    if transactions == []:
        yield []
    else:
        for transaction in transactions:
            yield transaction["description"]


def card_number_generator(start: int = 1, stop: int = 9999999999999999) -> str:
    """Функция генерирует номера банковских карт в заданном диапозоне"""
    if len(str(start)) <= 16 and len(str(stop)) <= 16:
        for gen_num in range(start, stop + 1):
            len_numbers = 16 - len(str(gen_num))
            if gen_num <= stop:
                card_number_gen = ("0" * len_numbers) + str(gen_num)
                card_number_gen = (
                    card_number_gen[:4]
                    + " "
                    + card_number_gen[4:8]
                    + " "
                    + card_number_gen[8:12]
                    + " "
                    + card_number_gen[-4:]
                )
                yield card_number_gen
    else:
        yield "Число не долно превышать 16 символов"

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_01(transactions):
    i = filter_by_currency(transactions, "RUB")
    assert next(i) == {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    }
    assert next(i) == {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    }


def test_filter_by_currency_02(transactions):
    i = filter_by_currency(transactions, '')
    assert next(i) == transactions


def test_transaction_descriptions_01(transactions):
    i = transaction_descriptions(transactions)
    assert next(i) == "Перевод организации"
    assert next(i) == "Перевод со счета на счет"
    assert next(i) == "Перевод со счета на счет"
    assert next(i) == "Перевод с карты на карту"
    assert next(i) == "Перевод организации"


def test_transaction_descriptions_02():
    i = transaction_descriptions([])
    assert next(i) == []


def test_card_number_generator_01():
    i = card_number_generator(1, 5)
    assert next(i) == "0000 0000 0000 0001"
    assert next(i) == "0000 0000 0000 0002"
    assert next(i) == "0000 0000 0000 0003"
    assert next(i) == "0000 0000 0000 0004"
    assert next(i) == "0000 0000 0000 0005"


def test_card_number_generator_02():
    i = card_number_generator(1, 78946561562131316516161)
    assert next(i) == "Число не долно превышать 16 символов"

from src.processing import filter_by_code, filter_by_state, process_bank_operations, process_bank_search, sort_by_date


def test_filter_by_state(list_1: list, list_2: list, list_3: list, list_4: list, state_c: str) -> None:
    assert filter_by_state(list_1) == [
        {"id": 346564543, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    assert filter_by_state(list_2, state_c) == [
        {"id": 41428829, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 78773733, "state": "CANCELED", "date": "2018-06-28T02:08:58.425572"},
        {"id": 234242415, "state": "CANCELED", "date": "2016-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2010-10-14T08:21:33.419441"},
    ]
    assert filter_by_state(list_3, state_c) == []
    assert filter_by_state(list_4) == []


def test_sort_by_date(list_1: list, list_2: list, list_3: list, list_4: list, reverse_f: bool) -> None:
    assert sort_by_date(list_1) == [
        {"id": 346564543, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 398738794, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    assert sort_by_date(list_2, reverse_f) == [
        {"id": 615064591, "state": "CANCELED", "date": "2010-10-14T08:21:33.419441"},
        {"id": 234242415, "state": "CANCELED", "date": "2016-09-12T21:27:25.241689"},
        {"id": 78773733, "state": "CANCELED", "date": "2018-06-28T02:08:58.425572"},
        {"id": 41428829, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
    ]
    assert sort_by_date(list_3) == [
        {"id": 735434344, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 727278758, "state": "EXECUTED", "date": "2017-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2015-06-30T02:08:58.425572"},
        {"id": 891192929, "state": "EXECUTED", "date": "2014-10-14T08:21:33.419441"},
    ]
    assert sort_by_date(list_4) == []


def test_filter_by_code(transactions: list) -> None:
    assert filter_by_code(transactions) == [
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]
    assert filter_by_code(transactions, "USD") == [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
    ]
    assert filter_by_code(transactions, "EUR") == []
    assert filter_by_code(None) == []
    assert filter_by_code([]) == []


def test_process_bank_search(transactions_1: list) -> None:
    assert process_bank_search(transactions_1, "открытие") == [
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431",
        },
        {
            "id": 596171168,
            "state": "EXECUTED",
            "date": "2018-07-11T02:26:18.671407",
            "operationAmount": {"amount": "79931.03", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Открытие вклада",
            "to": "Счет 72082042523231456215",
        },
        {
            "id": 863064926,
            "state": "EXECUTED",
            "date": "2019-12-08T22:46:21.935582",
            "operationAmount": {"amount": "41096.24", "currency": {"name": "USD", "code": "USD"}},
            "description": "Открытие вклада",
            "to": "Счет 90424923579946435907",
        },
    ]
    assert process_bank_search(transactions_1, "с карты на карту") == [
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        }
    ]
    assert process_bank_search(transactions_1, None) == transactions_1
    assert process_bank_search(transactions_1, "") == transactions_1
    assert process_bank_search(transactions_1, "rmor") == []


def test_process_bank_operations(transactions_1: list) -> None:
    assert process_bank_operations(transactions_1, ["Открытие вклада", "Перевод организации"]) == {
        "Открытие вклада": 3,
        "Перевод организации": 6,
    }
    assert process_bank_operations(transactions_1, []) == {
        "Перевод организации": 6,
        "Открытие вклада": 3,
        "Перевод со счета на счет": 2,
        "Перевод с карты на карту": 1,
    }
    assert process_bank_operations(transactions_1, None) == {
        "Перевод организации": 6,
        "Открытие вклада": 3,
        "Перевод со счета на счет": 2,
        "Перевод с карты на карту": 1,
    }

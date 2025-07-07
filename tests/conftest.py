import pytest


@pytest.fixture
def transactions():
    return [
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
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
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


@pytest.fixture
def number_1() -> str:
    return "1234567891011123"


@pytest.fixture
def number_2() -> str:
    return "8592504291019761"


@pytest.fixture
def number_3() -> str:
    return "9482197721097249"


@pytest.fixture
def number_4() -> str:
    return ""


@pytest.fixture
def date_1() -> str:
    return "2024-03-11T02:26:18.671407"


@pytest.fixture
def date_2() -> str:
    return "2020-05-08T02:26:18.671407"


@pytest.fixture
def date_3() -> str:
    return "2015-12-25T02:26:18.671407"


@pytest.fixture
def date_4() -> str:
    return ""


@pytest.fixture
def state_c() -> str:
    return "CANCELED"


@pytest.fixture
def reverse_f() -> bool:
    return False


@pytest.fixture
def list_1() -> list:
    return [
        {"id": 346564543, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 398738794, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def list_2() -> list:
    return [
        {"id": 41428829, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 78773733, "state": "CANCELED", "date": "2018-06-28T02:08:58.425572"},
        {"id": 234242415, "state": "CANCELED", "date": "2016-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2010-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def list_3() -> list:
    return [
        {"id": 735434344, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2015-06-30T02:08:58.425572"},
        {"id": 727278758, "state": "EXECUTED", "date": "2017-09-12T21:27:25.241689"},
        {"id": 891192929, "state": "EXECUTED", "date": "2014-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def list_4() -> list:
    return []

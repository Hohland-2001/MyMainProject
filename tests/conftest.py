import pytest


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

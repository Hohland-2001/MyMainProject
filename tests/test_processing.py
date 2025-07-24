from src.processing import filter_by_state, sort_by_date


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

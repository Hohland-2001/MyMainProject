import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(value: str, expected: str) -> None:
    assert mask_account_card(value) == expected


def test_get_date(date_1: str, date_2: str, date_3: str, date_4: str) -> None:
    assert get_date(date_1) == "11.03.2024"
    assert get_date(date_2) == "08.05.2020"
    assert get_date(date_3) == "25.12.2015"
    assert get_date(date_4) == ""

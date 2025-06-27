from datetime import datetime
from typing import List, Dict


def get_mask_card_number(number: str) -> str:
    """Функция маскирует номер карты"""
    mask_card_number = number[:4] + " " + number[4:6] + "** **** " + number[12:]
    return mask_card_number


def get_mask_account(number: str) -> str:
    """Функция маскирует номер счёта"""
    mask_account = number.replace(number[:-4], "**")
    return mask_account


def mask_account_card(number: str) -> str:
    number_list = number.split()
    if number_list[0] == "Счет":
        number_list[1] = get_mask_account(number_list[1])
    else:
        number_list[1] = get_mask_card_number(number_list[1])
    mask = " ".join(number_list)
    return mask


def get_date(date: str) -> str:
    new_date = date[8:10] + date[4:8] + date[:4]
    new_date = new_date.replace("-", ".")
    return new_date


def filter_by_state(list_of_dictionary: list, state="EXECUTED") -> list:
    new_list_of_dictionary = []
    for i in list_of_dictionary:
        if i["state"] == state:
            new_list_of_dictionary.append(i)
        else:
            continue
    return new_list_of_dictionary


def sort_by_date(operations: List[Dict[str, str]], reverse: bool = True) -> List[Dict[str, str]]:
    sorted_operations = operations.copy()
    sorted_operations.sort(key=lambda x: datetime.fromisoformat(x["date"]), reverse=reverse)
    return sorted_operations


print(
    sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)

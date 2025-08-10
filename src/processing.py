import re
from collections import Counter
from datetime import datetime


def filter_by_state(list_of_dictionary: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция возвращает новый список словарей по заданному значению ключа "state" (по умолчанию - "EXECUTED")"""
    new_list_of_dictionary = []
    for i in list_of_dictionary:
        if i.get("state") == state:
            new_list_of_dictionary.append(i)
        else:
            continue
    return new_list_of_dictionary


def filter_by_code(list_of_dictionary: list[dict], code: str = "RUB") -> list[dict]:
    """Функция возвращает спсиок словарей по заданному значению ключа 'code' (по умолчанию - RUB)"""
    new_list_of_dictionary = []
    for i in list_of_dictionary:
        if i["operationAmount"]["currency"]["code"] == code:
            new_list_of_dictionary.append(i)
        else:
            continue
    return new_list_of_dictionary


def sort_by_date(operations: list[dict], reverse: bool = True) -> list[dict]:
    """Функция возвращает список словарей, сортируемый по дате (по умолчанию - убывание)"""
    sorted_operations = operations.copy()
    sorted_operations.sort(key=lambda x: datetime.fromisoformat(x["date"]), reverse=reverse)
    return sorted_operations


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """
    Функцию, которая принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка
    """
    result_list = []
    for d in data:
        if d.keys() and re.search(f"{search}", d["description"], flags=re.IGNORECASE):
            result_list.append(d)
        else:
            continue
    return result_list


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """
    Функцию, которая принимает список словарей с данными о банковских операциях и
    список категорий операций, а возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории
    """
    list_categories = []
    for i in categories:
        for d in data:
            if i == d.get("description"):
                list_categories.append(i)
            else:
                continue
    return dict(Counter(list_categories))

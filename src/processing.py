from datetime import datetime
from typing import List, Dict


def filter_by_state(list_of_dictionary: list, state='EXECUTED') -> list:
    """Функция возвращает новый список словарей по заданному значению ключа"""
    new_list_of_dictionary = []
    for i in list_of_dictionary:
        if i['state'] == state:
            new_list_of_dictionary.append(i)
        else:
            continue
    return new_list_of_dictionary


def sort_by_date(operations: List[Dict[str, str]], reverse: bool = True) -> List[Dict[str, str]]:
    """Функция возвращает список словарей по дате (по умолчанию — убывание)"""
    sorted_operations = operations.copy()
    sorted_operations.sort(key=lambda x: datetime.fromisoformat(x["date"]), reverse=reverse)
    return sorted_operations

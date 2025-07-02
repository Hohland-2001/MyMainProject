from datetime import datetime


def filter_by_state(list_of_dictionary: list, state: str = "EXECUTED") -> list:
    """Функция возвращает новый список словарей по заданному значению ключа "state" (по умолчанию - "EXECUTED")"""
    new_list_of_dictionary = []
    for i in list_of_dictionary:
        if i["state"] == state:
            new_list_of_dictionary.append(i)
        else:
            continue
    return new_list_of_dictionary


def sort_by_date(operations: list, reverse: bool = True) -> list:
    """Функция возвращает список словарей, сортируемый по дате (по умолчанию - убывание)"""
    sorted_operations = operations.copy()
    sorted_operations.sort(key=lambda x: datetime.fromisoformat(x["date"]), reverse=reverse)
    return sorted_operations

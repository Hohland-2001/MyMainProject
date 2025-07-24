import json


def get_list_of_operations(path_to_json: str | None) -> list[dict]:
    """Функция возвращает список операций"""
    try:
        with open(path_to_json, encoding="utf-8") as json_file:
            try:
                data = json.load(json_file)
                if type(data) is not list:
                    return []
                else:
                    return data
            except json.JSONDecodeError:
                return []
    except FileNotFoundError:
        return []


print(get_list_of_operations("../data/operations.json"))

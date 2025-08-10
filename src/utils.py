import json
import logging

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/utils.log", encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_operations_from_json(path_to_json: str | None = "../data/operations.json") -> list[dict]:
    """Функция возвращает список операций из json-файла"""
    try:
        with open(path_to_json, encoding="utf-8") as json_file:
            logger.info(f"Попытка открытие файла {path_to_json}")
            try:
                logger.info(f"Формирование списка операций из файла {path_to_json}")
                data = json.load(json_file)
                if type(data) is not list:
                    return []
                else:
                    logger.info("Получен список операций")
                    return data
            except json.JSONDecodeError as je:
                logger.error(f"Произошла ошибка {je}. Возврат пустого списка")
                return []
    except FileNotFoundError as e:
        logger.error(f"Произошла ошибка {e}. Возврат пустого списка")
        return []

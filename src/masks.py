import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("../logs/masks.log", encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(number: str) -> str:
    """Функция получает на вход номер карты и маскирует его"""
    try:
        logger.info(f"Процесс маскировки номера карты {number}")
        if number == "":
            return ""
        else:
            mask_card_number = number[:4] + " " + number[4:6] + "** **** " + number[12:]
            logger.info(f"Завершение процесса маскировки карты {mask_card_number}")
            return mask_card_number
    except Exception as e:
        logging.error(f"Произошла ошибка {e}")


def get_mask_account(number: str) -> str:
    """Функция получает на вход номер счёта и маскирует его"""
    try:
        logger.info(f"Процесс маскировки счёта {number}")
        if number == "":
            return ""
        else:
            mask_account = number.replace(number[:-4], "**")
            logger.info(f"Завершение процесса маскировки счёта {mask_account}")
            return mask_account
    except Exception as e:
        logger.info(f"Приизошла ошибка {e}")


print(get_mask_card_number("1234323443460957"))

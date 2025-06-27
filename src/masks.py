def get_mask_card_number(number: str) -> str:
    """Функция получает на вход номер карты и маскирует его"""
    mask_card_number = number[:4] + " " + number[4:6] + "** **** " + number[12:]
    return mask_card_number


def get_mask_account(number: str) -> str:
    """Функция получает на вход номер счёта и маскирует его"""
    mask_account = number.replace(number[:-4], "**")
    return mask_account

def get_mask_card_number(number: str) -> str:
    """Функция маскирует номер карты"""
    mask_card_number = number[:4] + " " + number[4:6] + "** **** " + number[12:]
    return mask_card_number


def get_mask_account(number: str) -> str:
    """Функция маскирует номер счёта"""
    mask_account = number.replace(number[:-4], "**")
    return mask_account

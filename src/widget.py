from masks import get_mask_account, get_mask_card_number


def mask_account_card(number: str) -> str:
    """Функция маскирует номер или счёт, используя функции из модуля /masks"""
    number_list = number.split()
    if number_list[0] == 'Счет':
        number_list[1] = get_mask_account(number_list[1])
    else:
        number_list[1] = get_mask_card_number(number_list[1])
    mask = ' '.join(number_list)
    return mask


def get_date(date: str) -> str:
    """Функция преобразует дату в формат ДД.ММ.ГГГГ"""
    new_date = date[8:10] + date[4:8] + date[:4]
    new_date = new_date.replace('-', '.')
    return new_date
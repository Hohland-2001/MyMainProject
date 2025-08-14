from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number: str) -> str:
    """Функция маскирует номер карты или счёт, используя функции из модуля masks"""
    number_list = str(number).split()
    if number_list[0] == "Счет":
        number_list[1] = get_mask_account(number_list[1])
    else:
        count = 0
        for i in number_list:
            if i.isalpha():
                count += 1
                continue
            else:
                number_list[count] = get_mask_card_number(i)
    mask_account = " ".join(number_list)
    return mask_account


def get_date(date: str) -> str:
    """Функция преобразует дату в формат ДД.ММ.ГГГГ"""
    new_date = date[8:10] + date[4:8] + date[:4]
    new_date = new_date.replace("-", ".")
    return new_date

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(number_1: str, number_2: str, number_3: str, number_4: str) -> str:
    assert get_mask_card_number(number_1) == "1234 56** **** 1123"
    assert get_mask_card_number(number_2) == "8592 50** **** 9761"
    assert get_mask_card_number(number_3) == "9482 19** **** 7249"
    assert get_mask_card_number(number_4) == ""


def test_get_mask_account(number_1: str, number_2: str, number_3: str, number_4: str) -> str:
    assert get_mask_account(number_1) == "**1123"
    assert get_mask_account(number_2) == "**9761"
    assert get_mask_account(number_3) == "**7249"
    assert get_mask_account(number_4) == ""

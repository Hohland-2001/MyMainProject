import json
from unittest.mock import Mock, patch

from src.utils import get_list_of_operations

list_transaction = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
]


@patch("builtins.open", create=True)
def test_get_list_of_operations(mock_open):
    mock_file = mock_open.return_value.__enter__.return_value
    mock_file.read.return_value = "[]"
    assert get_list_of_operations("test.txt") == []

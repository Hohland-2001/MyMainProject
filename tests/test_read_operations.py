from unittest.mock import patch

import pandas

from src.read_operations import read_operations_from_csv


@patch("pandas.read_csv")
def test_read_operations_from_csv(mock_get):
    mock_get_return_value = {
        "id": [650703],
        "state": ["EXECUTED"],
        "date": ["2023-09-05T11:30:32Z"],
        "amount": ["16210"],
        "name": ["Sol"],
        "code": ["PEN"],
        "from": ["Счет 58803664561298323391"],
        "to": ["Счет 39745660563456619397"],
        "description": ["Перевод организации"],
    }
    mock_get.return_value = pandas.DataFrame(mock_get_return_value)
    data_csv = "transac.csv"
    assert read_operations_from_csv(data_csv) == [
        {
            "id": 650703,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "operationAmount": {"amount": "16210", "currency": {"name": "Sol", "code": "PEN"}},
            "description": "Перевод организации",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
        }
    ]

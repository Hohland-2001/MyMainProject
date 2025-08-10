from unittest.mock import patch

from src.utils import read_operations_from_json


@patch("builtins.open", create=True)
def test_get_list_of_operations(mock_open):
    mock_file = mock_open.return_value.__enter__.return_value
    mock_file.read.return_value = "[]"
    assert read_operations_from_json("test.txt") == []

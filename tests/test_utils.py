from unittest.mock import patch

from src.utils import get_list_of_operations


@patch("builtins.open", create=True)
def test_get_list_of_operations(mock_open):
    mock_file = mock_open.return_value.__enter__.return_value
    mock_file.read.return_value = "[]"
    assert get_list_of_operations("test.txt") == []

from unittest.mock import patch

from pokefunctions import get_all, add_one

@patch("pokefunctions.conn")
def test_get_all_returns_list(mock_connection):
    """With a cursor"""

    mock_cur = mock_connection.cursor
    mock_with_cur = mock_cur.return_value.__enter__
    mock_with_cur_execute = mock_with_cur.return_value.execute
    mock_with_cur.return_value.fetchall.return_value = []

    
    result = get_all()

    assert isinstance(result, list)
    mock_with_cur_execute.assert_called()
    mock_with_cur_execute.assert_called_with("SELECT * FROM pokemon;")

@patch("pokefunctions.conn")
def test_add_one_makes_correct_sql(mock_connection):
    """Without a cursor"""

    mock_cur = mock_connection.cursor
    mock_cur_execute = mock_cur.return_value.execute
    mock_cur.return_value.fetchall.return_value = []

    result = add_one({ "name": "Aalanicorn", "height": 1, "weight": 1 })

    mock_cur_execute.assert_called()
    assert "Aalanicorn" in str(mock_cur_execute.call_args_list[1])


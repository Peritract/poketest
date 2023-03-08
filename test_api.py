from unittest.mock import patch

@patch("pokefunctions.get_all")
def test_pokemon_get_returns_a_list(mock_get_all, test_api):

    # Intercept any request to pokefunctions.get_all()
    mock_get_all.return_value = [{"a": 1}, {"b": 2}]

    result = test_api.get("/pokemon")
    data = result.json

    assert isinstance(data, list)
    assert all([isinstance(row, dict) for row in data])


@patch("pokefunctions.get_all")
def test_pokemon_get_fails_on_exception(mock_get_all, test_api):

    mock_get_all.side_effect = Exception("Aargh! A problem!")

    result = test_api.get("/pokemon")

    assert result.status_code == 500
    assert type(result.json['error']) == bool and result.json['error']


@patch("pokefunctions.add_one")
def test_pokemon_post_returns_expected_response(mock_add_one, test_api):

    mock_add_one.return_value = {"name": "Tobara"}

    result = test_api.post("/pokemon", json={"name": "Tobara"})
    data = result.json

    assert result.status_code == 201
    assert isinstance(data, dict)

@patch("pokefunctions.add_one")
def test_pokemon_post_returns_400_on_empty_body(mock_add_one, test_api):

    result = test_api.post("/pokemon")
    data = result.json

    assert result.status_code == 400

@patch("pokefunctions.add_one")
def test_pokemon_post_returns_400_on_malformed_body(mock_add_one, test_api):

    result = test_api.post("/pokemon", json={ "not": "the", "right": "keys"})
    data = result.json

    assert result.status_code == 400
    assert data["Message"] == "Invalid post body"
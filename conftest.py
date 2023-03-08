import pytest

from api import api

@pytest.fixture
def test_api():
    return api.test_client()
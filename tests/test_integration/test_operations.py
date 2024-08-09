import requests
import pytest


@pytest.fixture
def base_url():
    # Define the base URL for your service
    return "http://localhost:8080"


def test_get_root(base_url):
    response = requests.get(f"{base_url}/elixircoud/csh/v1")

    assert (
        response.status_code == 200
    ), f"Expected status code 200, got {response.status_code}"

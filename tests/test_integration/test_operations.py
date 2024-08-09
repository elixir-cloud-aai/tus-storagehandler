"""Integration tests for operations in the service."""

import pytest
import requests

SUCCESS_STATUS_CODE = 200


@pytest.fixture
def base_url():
    """Return the base URL for the service."""
    return "http://localhost:8080"


def test_get_root(base_url):
    """Test the root endpoint of the service."""
    response = requests.get(f"{base_url}/elixircoud/csh/v1")

    assert (
        response.status_code == SUCCESS_STATUS_CODE
    ), f"Expected status code 200, got {response.status_code}"

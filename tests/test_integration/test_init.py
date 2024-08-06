"""Integration tests for the __init__.py file."""

from pathlib import Path


def test_init_file_exists():
    """Check if the __init__.py file exists."""
    path_to_init_file = Path(__file__).parents[2] / "tus_storagehandler" / "__init__.py"
    assert path_to_init_file.exists(), f"File {path_to_init_file} does not exist."

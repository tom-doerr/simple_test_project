"""Test Textual version compatibility."""
import importlib.metadata
import pytest

def test_textual_version():
    """Ensure Textual version meets minimum requirements."""
    try:
        version = importlib.metadata.version("textual")
    except importlib.metadata.PackageNotFoundError:
        pytest.skip("Textual not installed")
    
    # Handle both 0.x and 1.x+ version formats
    parts = list(map(int, version.split('.')))
    assert (parts[0] > 0) or (parts[0] == 0 and parts[1] >= 40), \
        f"Textual 0.40.0 or newer required (found {version})"

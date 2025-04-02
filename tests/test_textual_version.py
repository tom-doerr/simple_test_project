"""Test Textual version compatibility."""
import importlib.metadata
import pytest

def test_textual_version():
    """Ensure Textual version meets minimum requirements."""
    try:
        version = importlib.metadata.version("textual")
    except importlib.metadata.PackageNotFoundError:
        pytest.skip("Textual not installed")
    
    major, minor, _ = version.split('.', 2)
    assert int(major) >= 0 and int(minor) >= 40, "Textual 0.40.0 or newer required"

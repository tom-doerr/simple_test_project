"""Tests for show_time.py."""

import subprocess

import pytest
from textual.testing import AppTester

try:
    from show_time import CryptoApp, CryptoDisplay
except ImportError:
    print("Failed to import CryptoApp from show_time.py. Ensure textual is installed.")
    CryptoApp = None
    CryptoDisplay = None


def test_show_time():
    """Test that show_time.py runs without errors."""
    result = subprocess.run(
        ["python", "show_time.py"], capture_output=True, text=True, check=True
    )
    assert result.returncode == 0


def test_show_time_output():
    """Test that show_time.py produces output and contains expected data."""
    result = subprocess.run(
        ["python", "show_time.py"], capture_output=True, text=True, check=True
    )
    assert len(result.stdout) > 0
    assert "Ethereum" in result.stdout
    assert "$" in result.stdout


def test_textual_app_runs():
    """Test that the Textual app runs without errors."""
    result = subprocess.run(
        ["python", "show_time.py", "--textual"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0


@pytest.mark.asyncio
async def test_crypto_display_render():
    """Test that CryptoDisplay renders correctly."""
    if CryptoApp is None:
        pytest.skip("CryptoApp could not be imported.")

    app = AppTester(app=CryptoApp())
    await app.boot_app()
    assert app.content != ""


@pytest.mark.asyncio
async def test_crypto_display_initial_render():
    """Test that CryptoDisplay renders initial content correctly."""
    if CryptoApp is None or CryptoDisplay is None:
        pytest.skip("CryptoApp or CryptoDisplay could not be imported.")

    app = AppTester(app=CryptoApp())
    await app.boot_app()
    crypto_display = app.app.query_one(CryptoDisplay)
    assert "Loading..." in str(crypto_display.render())


@pytest.mark.asyncio
async def test_crypto_display_price_displayed():
    """Test that CryptoDisplay displays the Ethereum price."""
    if CryptoApp is None or CryptoDisplay is None:
        pytest.skip("CryptoApp or CryptoDisplay could not be imported.")

    app = AppTester(app=CryptoApp())
    await app.boot_app()
    crypto_display = app.app.query_one(CryptoDisplay)
    await crypto_display.update_price()  # Wait for the price to load
    assert "$" in str(crypto_display.render())

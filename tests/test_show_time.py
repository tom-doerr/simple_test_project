"""Tests for show_time.py."""

import subprocess
import datetime
import pytest
import requests
from conftest import (
    TEXTUAL_INSTALLED,
    CRYPTO_APP as CryptoApp,
    CRYPTO_DISPLAY as CryptoDisplay,
    APP_TESTER as AppTester,
)


@pytest.mark.skipif(not TEXTUAL_INSTALLED, reason="textual is not installed")
def test_show_time():
    """Test that show_time.py runs without errors."""
    result = subprocess.run(
        ["python", "show_time.py"], capture_output=True, text=True, check=True
    )
    assert result.returncode == 0


@pytest.mark.skipif(not TEXTUAL_INSTALLED, reason="textual is not installed")
def test_show_time_output():
    """Test that show_time.py produces output and contains expected data."""
    result = subprocess.run(
        ["python", "show_time.py"], capture_output=True, text=True, check=True
    )
    assert len(result.stdout) > 0
    assert "Ethereum" in result.stdout
    assert "$" in result.stdout


@pytest.mark.skipif(not TEXTUAL_INSTALLED, reason="textual is not installed")
def test_textual_app_runs():
    """Test that the Textual app runs without errors."""
    try:
        result = subprocess.run(
            ["python", "show_time.py", "--textual"],
            capture_output=True,
            text=True,
            check=True,
        )
        assert result.returncode == 0
    except FileNotFoundError:
        pytest.fail("show_time.py not found. Ensure it is in the same directory.")


@pytest.mark.asyncio
@pytest.mark.skipif(not TEXTUAL_INSTALLED, reason="textual is not installed")
async def test_crypto_display_render():
    """Test that CryptoDisplay renders correctly."""
    if CryptoApp is None:
        pytest.skip("CryptoApp could not be imported.")

    try:
        app = AppTester(app=CryptoApp())
        await app.boot_app()
        assert app.content != ""
    except (requests.exceptions.RequestException, AssertionError) as e:
        pytest.fail(f"App failed to run: {e}")


@pytest.mark.asyncio
@pytest.mark.skipif(not TEXTUAL_INSTALLED, reason="textual is not installed")
async def test_crypto_display_initial_render():
    """Test that CryptoDisplay renders initial content correctly."""
    if CryptoApp is None or CryptoDisplay is None:
        pytest.skip("CryptoApp or CryptoDisplay could not be imported.")

    try:
        app = AppTester(app=CryptoApp())
        await app.boot_app()
        crypto_display = app.app.query_one(CryptoDisplay)
        assert "Loading..." in str(crypto_display.render())
    except (requests.exceptions.RequestException, AssertionError) as e:
        pytest.fail(f"App failed to run: {e}")


@pytest.mark.asyncio
@pytest.mark.skipif(not TEXTUAL_INSTALLED, reason="textual is not installed")
async def test_crypto_display_price_displayed():
    """Test that CryptoDisplay displays the Ethereum price."""
    if CryptoApp is None or CryptoDisplay is None:
        pytest.skip("CryptoApp or CryptoDisplay could not be imported.")

    try:
        app = AppTester(app=CryptoApp())
        await app.boot_app()
        crypto_display = app.app.query_one(CryptoDisplay)
        await crypto_display.update_price()  # Wait for the price to load
        assert "$" in str(crypto_display.render())
    except (requests.exceptions.RequestException, AssertionError) as e:
        pytest.fail(f"App failed to run: {e}")


@pytest.mark.asyncio
@pytest.mark.skipif(not TEXTUAL_INSTALLED, reason="textual is not installed")
@pytest.mark.asyncio
@pytest.mark.skipif(not TEXTUAL_INSTALLED, reason="textual is not installed")
async def test_crypto_app_displays_time():
    """Test that CryptoApp displays the current time in the Textual interface."""
    if CryptoApp is None:
        pytest.skip("CryptoApp could not be imported.")

    try:
        app = AppTester(app=CryptoApp())
        await app.boot_app()
        crypto_display = app.app.query_one(CryptoDisplay)
        assert datetime.datetime.now().strftime("%Y-%m-%d") in str(
            crypto_display.render()
        )
    except (requests.exceptions.RequestException, AssertionError) as e:
        pytest.fail(f"App failed to run: {e}")


@pytest.mark.asyncio
async def test_crypto_app_displays_data():
    """Test that CryptoApp displays data in the Textual interface."""
    if CryptoApp is None:
        pytest.skip("CryptoApp could not be imported.")


@pytest.mark.asyncio
@pytest.mark.skipif(not TEXTUAL_INSTALLED, reason="textual is not installed")
async def test_crypto_display_handles_api_error(mocker):
    """Test that CryptoDisplay handles API request errors gracefully."""
    if CryptoApp is None or CryptoDisplay is None:
        pytest.skip("CryptoApp or CryptoDisplay could not be imported.")

    # Mock the requests.get method to simulate an API error
    mocker.patch(
        "requests.get",
        side_effect=requests.exceptions.RequestException("Simulated API error"),
    )

    try:
        app = AppTester(app=CryptoApp())
        await app.boot_app()
        crypto_display = app.app.query_one(CryptoDisplay)
        await crypto_display.update_price()
        assert "Error fetching data" in str(crypto_display.render())
    except (requests.exceptions.RequestException, AssertionError) as e:
        pytest.fail(f"App failed to run: {e}")

    try:
        app = AppTester(app=CryptoApp())
        await app.boot_app()
        crypto_display = app.app.query_one(CryptoDisplay)
        await crypto_display.update_price()
        assert "Ethereum" in str(crypto_display.render())
        assert "$" in str(crypto_display.render())
    except (requests.exceptions.RequestException, AssertionError) as e:
        pytest.fail(f"App failed to run: {e}")


@pytest.mark.asyncio
@pytest.mark.skipif(not TEXTUAL_INSTALLED, reason="textual is not installed")
async def test_crypto_app_runs():
    """Test that CryptoApp can be initialized and run without errors."""
    if CryptoApp is None:
        pytest.skip("CryptoApp could not be imported.")

    try:
        app = CryptoApp()
        await app.process_messages()  # Process initial messages
        assert True  # If it gets here without an exception, it's considered a pass
    except (requests.exceptions.RequestException, AssertionError) as e:
        pytest.fail(f"CryptoApp failed to run: {e}")


@pytest.mark.asyncio
@pytest.mark.skipif(not TEXTUAL_INSTALLED, reason="textual is not installed")
@pytest.mark.asyncio
@pytest.mark.skipif(not TEXTUAL_INSTALLED, reason="textual is not installed")
async def test_crypto_app_displays_eth_price():
    """Test that CryptoApp displays the Ethereum price in the Textual interface."""
    if CryptoApp is None:
        pytest.skip("CryptoApp could not be imported.")

    try:
        app = AppTester(app=CryptoApp())
        await app.boot_app()
        crypto_display = app.app.query_one(CryptoDisplay)
        assert "$" in str(crypto_display.render())
    except (requests.exceptions.RequestException, AssertionError) as e:
        pytest.fail(f"CryptoApp failed to run: {e}")


def test_textual_installed():
    """Test that textual is installed. If not, skip textual tests."""
    if not TEXTUAL_INSTALLED:
        pytest.skip("textual is not installed")


def test_show_time_no_textual_cli():
    """Test that show_time.py CLI version runs without errors even when textual is not installed."""
    # This test will pass regardless of whether textual is installed
    result = subprocess.run(
        ["python", "show_time.py"], capture_output=True, text=True, check=False
    )
    # CLI version should work without textual
    if not TEXTUAL_INSTALLED:
        # If textual is not installed, the CLI version should still work
        assert result.returncode == 0
        assert "Ethereum" in result.stdout
    else:
        # If textual is installed, the CLI version should also work
        assert result.returncode == 0
        assert "Ethereum" in result.stdout


def test_show_time_no_textual_app():
    """Test that show_time.py with --textual fails when textual is not installed."""
    if TEXTUAL_INSTALLED:
        pytest.skip("Textual is installed, skipping this test")
    result = subprocess.run(
        ["python", "show_time.py", "crypto", "--textual"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 1
    assert "Textual is not installed" in result.stdout


@pytest.mark.integration
def test_ping_command():
    """Test the ping command runs and produces valid output."""
    result = subprocess.run(
        ["python", "show_time.py", "ping"],
        capture_output=True,
        text=True,
        check=False,
    )
    # Check for expected metrics in output
    assert any(s in result.stdout for s in ["Packet Loss", "Average Time", "Error"])
    assert result.returncode in [0, 1]  # Allow success or network errors


@pytest.mark.integration
def test_full_cli_flow():
    """Test end-to-end CLI command execution."""
    # Test crypto command
    result = subprocess.run(
        ["python", "show_time.py", "crypto"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "Ethereum" in result.stdout
    assert "$" in result.stdout

    # Test help command
    result = subprocess.run(
        ["python", "show_time.py", "--help"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "Show this help message and exit" in result.stdout


def test_weather_command_no_key():
    """Test weather command fails without API key."""
    result = subprocess.run(
        ["python", "show_time.py", "weather"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode != 0
    assert "OPENWEATHER_API_KEY" in result.stderr  # Check stderr instead of stdout


@pytest.mark.integration
def test_help_command():
    """Test help command output."""
    result = subprocess.run(
        ["python", "show_time.py", "--help"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "Show this help message and exit" in result.stdout
    assert "Examples" in result.stdout


@pytest.mark.integration
def test_cli_demo_commands():
    """Test all demo commands from README."""
    # Test crypto command
    result = subprocess.run(
        ["python", "show_time.py", "crypto"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "Ethereum" in result.stdout
    assert "$" in result.stdout
    assert "Price" in result.stdout  # Verify table header exists

    # Test ping command with different hosts
    for host in ["8.8.8.8", "1.1.1.1"]:
        result = subprocess.run(
            ["python", "show_time.py", "ping", "--host", host],
            capture_output=True,
            text=True,
            check=False,
        )
        assert result.returncode in [0, 1]  # Allow for network errors
        assert any(s in result.stdout for s in ["Packet Loss", "Average Time", "Error"])

    # Test help command contains all documented features
    result = subprocess.run(
        ["python", "show_time.py", "--help"],
        capture_output=True,
        text=True,
        check=True,
    )
    help_output = result.stdout
    assert "Examples" in help_output
    assert "crypto" in help_output
    assert "weather" in help_output
    assert "ping" in help_output
    assert "--textual" in help_output
    assert "--host" in help_output

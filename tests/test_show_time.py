"""Tests for show_time.py."""

import subprocess
import datetime


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
        ["python", "show_time.py", "--textual"], capture_output=True, text=True, check=True
    )
    assert result.returncode == 0

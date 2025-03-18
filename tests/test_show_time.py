"""Tests for show_time.py."""
import subprocess


def test_show_time():
    """Test that show_time.py runs without errors."""
    result = subprocess.run(
        ["python", "show_time.py"], capture_output=True, text=True, check=True
    )
    assert result.returncode == 0


def test_show_time_output():
    """Test that show_time.py produces output."""
    result = subprocess.run(
        ["python", "show_time.py"], capture_output=True, text=True, check=True
    )
    assert len(result.stdout) > 0

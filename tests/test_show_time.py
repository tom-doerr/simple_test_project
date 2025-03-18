import subprocess

def test_show_time():
    result = subprocess.run(['python', 'show_time.py'], capture_output=True, text=True, check=True)
    assert result.returncode == 0

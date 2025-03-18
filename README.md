# System Monitoring CLI

Track cryptocurrency prices, network status, and weather in your terminal!

## Features

- 🪙 Real-time Ethereum price tracking
- 🌤️ Local weather reports (requires OpenWeather API key)
- 📡 Network connectivity testing (ping jitter/loss)
- 🖥️ Text-based UI (TUI) mode with --textual flag
- 📊 Rich terminal output formatting

## Installation

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
# Basic crypto price display
python show_time.py crypto

# Crypto prices in Textual UI
python show_time.py crypto --textual

# Weather report (requires OPENWEATHER_API_KEY)
export OPENWEATHER_API_KEY="your_api_key"
python show_time.py weather

# Network connectivity test
python show_time.py ping --host 1.1.1.1

# Show help
python show_time.py --help
```

## Configuration

Set environment variables in your shell or `.env` file:
```bash
export OPENWEATHER_API_KEY="your_api_key_here"
```

## Development

Run tests:
```bash
pytest -v tests/
```

Lint code:
```bash
pylint *.py tests/*.py
```

## Demo

```bash
# Basic crypto price check
python show_time.py crypto

# Network test for Google DNS
python show_time.py ping --host 8.8.8.8

# Full integration test suite
pytest -v tests/test_show_time.py -m integration
```

> **Note**  
> The Textual interface requires Python 3.11+ and proper terminal support

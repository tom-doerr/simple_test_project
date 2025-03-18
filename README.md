# System Monitor CLI

Track cryptocurrency prices, network status, and weather from the command line.

## Features

- (Coin) Real-time Ethereum price tracking (CLI and TUI)
- 🌦️ Local weather reports via OpenWeatherMap API
- 📶 Network connectivity testing with ping statistics
- 🖥️ Textual-based Terminal User Interface (TUI)
- 📊 Rich formatted output with tables and colors
- ✅ Comprehensive test suite with 85%+ coverage

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python show_time.py [COMMAND] [OPTIONS]
```

### Key Commands

| Command | Description                                | Example                     |
|---------|--------------------------------------------|-----------------------------|
| crypto  | Show Ethereum price                        | `python show_time.py crypto --textual` |
| weather | Show local weather                         | `python show_time.py weather`          |
| ping    | Test network connectivity                  | `python show_time.py ping --host 8.8.8.8` |

### Demos

```bash
# Start Textual TUI interface
python show_time.py crypto --textual

# Get weather report (requires API key)
OPENWEATHER_API_KEY="your_key" python show_time.py weather

# Test network connection to Cloudflare DNS
python show_time.py ping --host 1.1.1.1
```

## Configuration

1. Get OpenWeatherMap API key: https://openweathermap.org/api
2. Set environment variable:
```bash
export OPENWEATHER_API_KEY="your_api_key_here"
```

## Testing & Quality

```bash
# Run all tests with coverage
pytest -v tests/ --cov=show_time --cov-report=term-missing

# Run linting checks
pylint show_time.py tests/

# Run type checking
mypy show_time.py
```

## Requirements

- Python 3.11+
- Terminal with true color support
- Internet connection for API calls

> **Warning**  
> The weather command requires a valid OpenWeatherMap API key.  
> Textual TUI requires a compatible terminal emulator.

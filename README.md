# System Monitor CLI

Track cryptocurrency prices, network status, and weather from the command line.

## Features

- Real-time Ethereum price tracking
- Local weather reports
- Network connectivity testing
- Textual TUI interface (requires textual)
- Rich terminal formatting
- Cross-platform support

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
# Show crypto prices (CLI)
python show_time.py crypto

# Show crypto prices (TUI)
python show_time.py crypto --textual

# Show weather report
python show_time.py weather

# Run network tests
python show_time.py ping --host 1.1.1.1

# Show help
python show_time.py --help
```

## Examples

Basic monitoring:
```bash
# Monitor crypto prices in TUI mode
python show_time.py crypto --textual

# Check weather and network status
python show_time.py weather
python show_time.py ping --host 8.8.8.8
```

Integration testing:
```bash
# Run all tests
pytest -v tests/

# Run network tests only
pytest -v tests/test_show_time.py -m integration
```

## Configuration

```bash
# Required for weather command
export OPENWEATHER_API_KEY="your_api_key_here"
```

> **Note**  
> The Textual interface requires Python 3.11+ and a compatible terminal

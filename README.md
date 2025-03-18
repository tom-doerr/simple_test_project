# System Monitor CLI

A command-line tool for monitoring cryptocurrency prices, network status, and weather information with both CLI and Textual TUI interfaces.

## Features

- Cryptocurrency price tracking (Ethereum)
- Local weather reports using OpenWeatherMap
- Network ping/jitter measurement
- Textual-based TUI interface (optional)

## Installation

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
# CLI crypto price
python show_time.py crypto

# TUI crypto price (requires textual)
python show_time.py crypto --textual

# Weather information (requires OPENWEATHER_API_KEY)
python show_time.py weather

# Network ping test
python show_time.py ping

# Show full help
python show_time.py --help
```

## Requirements

- Python 3.8+
- [Optional] Textual for TUI interface: `pip install textual`
- OpenWeatherMap API key for weather features

## Testing

```bash
# Run all tests
pytest -v

# Run CLI tests only
pytest -v tests/test_show_time.py -m "not textual"

# Run integration tests
pytest -v tests/test_show_time.py -m "integration"
```

## Demo

![CLI Demo](demo.gif) (requires demo.gif file)

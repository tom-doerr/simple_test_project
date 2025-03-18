# System Monitor CLI

A command-line tool to monitor cryptocurrency prices, network status, and weather.

## Features

- Real-time Ethereum price tracking
- Network connectivity testing (ping jitter)
- Local weather reports
- Text-based UI (TUI) mode when Textual is installed

## Installation

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
# Show Ethereum price (CLI mode)
python show_time.py crypto

# Start TUI mode (requires Textual)
python show_time.py crypto --textual

# Run network tests
python show_time.py ping

# Get weather report (requires OPENWEATHER_API_KEY)
OPENWEATHER_API_KEY=your_key python show_time.py weather

# Show help
python show_time.py --help
```

## Examples

![CLI Screenshot](https://via.placeholder.com/600x200.png?text=CLI+Demo)  
![TUI Screenshot](https://via.placeholder.com/600x200.png?text=TUI+Demo)

## Configuration

Set environment variables:
```bash
export OPENWEATHER_API_KEY="your_api_key_here"
```

## Development

Run tests:
```bash
pytest --cov=show_time --cov-report=term-missing tests/
```

## Requirements

- Python 3.8+
- See requirements.txt for dependencies

# System Monitoring CLI

Track cryptocurrency prices, network status, and weather information through both CLI and Textual TUI interfaces.

## Features

- Real-time Ethereum price tracking
- Network connectivity testing with ping statistics
- Local weather reporting
- Textual-based Terminal User Interface (TUI)
- Rich formatted output for CLI
- Automated integration tests

## Installation

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Environment Setup

```bash
# For weather functionality
export OPENWEATHER_API_KEY='your-api-key-here'

# For textual interface
pip install "textual==0.34.2"
```

## Usage

```bash
# Show crypto prices (CLI)
python show_time.py crypto

# Start TUI interface (requires textual)
python show_time.py crypto --textual

# Run network tests
python show_time.py ping

# Show weather info
python show_time.py weather

# Display help
python show_time.py --help
```

## Testing

Run the full test suite:
```bash
pytest -v tests/ --cov=show_time --cov-report=term-missing
```

## Demo Commands

```bash
# Basic crypto price display
python show_time.py crypto

# Network connectivity test
python show_time.py ping

# Help documentation
python show_time.py --help
```

![CLI Demo](https://via.placeholder.com/600x200.png?text=System+Monitoring+CLI)
![TUI Demo](https://via.placeholder.com/600x200.png?text=Textual+Interface)

## Requirements

- Python 3.11+
- Reliable internet connection
- See requirements.txt for package dependencies

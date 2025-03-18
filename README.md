# System Monitor CLI

A command-line tool to monitor cryptocurrency prices, network jitter, and weather information.

## Features

- Real-time Ethereum price from CoinGecko
- Current time display
- Network ping jitter measurement
- Local weather information (requires OpenWeatherMap API key)
- Textual TUI interface

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
# Display crypto prices (CLI table view)
python show_time.py crypto

# Start Textual UI for crypto prices
python show_time.py crypto --textual

# Show weather information
export OPENWEATHER_API_KEY="your_api_key"
python show_time.py weather

# Measure network jitter to New York server
python show_time.py ping
```

## Demo

![CLI Demo](demo.gif)

## Requirements

- Python 3.8+
- [Get OpenWeatherMap API Key](https://openweathermap.org/api)

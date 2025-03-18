"""Display current time and Ethereum price.

This module provides both a command-line interface and a Textual GUI
to display cryptocurrency prices and current time.
"""

import argparse
import datetime
import os
import sys
import requests
from rich.console import Console
from rich.table import Table


def get_current_location() -> dict:
    """Get current location using IP API."""
    try:
        resp = requests.get("https://ipapi.co/json/", timeout=10)
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.RequestException as e:
        local_console = Console()
        local_console.print(f"Error getting location: {e}", style="red")
        sys.exit(1)


def get_weather(owm_api_key: str, lat: float, lon: float) -> dict:
    """Get weather data from OpenWeatherMap API."""
    try:
        url = (
            f"http://api.openweathermap.org/data/2.5/weather"
            f"?lat={lat}&lon={lon}&appid={owm_api_key}&units=metric"
        )
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.RequestException as e:
        local_console = Console()
        local_console.print(f"Error fetching weather: {e}", style="red")
        sys.exit(1)


now = datetime.datetime.now()

# Check if textual is installed
TEXTUAL_INSTALLED = False
try:
    from textual.app import App
    from textual.widgets import Header, Footer, Static
    from textual import ComposeResult

    TEXTUAL_INSTALLED = True

    CSS_PATH = "crypto.tcss"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    class CryptoApp(App):
        """A Textual app to display crypto prices."""

        def compose(self) -> ComposeResult:
            """Create child widgets for the app."""
            yield Header()
            yield CryptoDisplay()
            yield Footer()

    class CryptoDisplay(Static):
        """A widget to display the crypto price."""

        def __init__(self):
            super().__init__("")  # Initialize with empty renderable
            self.eth_price = None
            self.current_time = None

        def on_mount(self) -> None:
            """Initialize price updates when the widget is mounted.

            Sets up a timer to refresh the crypto price every 60 seconds.
            """
            self.update_price()
            self.set_interval(60, self.update_price)

        async def update_price(self) -> None:
            """Fetch the latest Ethereum price and update the display."""
            try:
                api_response = requests.get(
                    "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd",
                    timeout=10,
                )
                api_response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
                api_data = api_response.json()
                self.eth_price = api_data["ethereum"]["usd"]
                self.current_time = datetime.datetime.now()
                self.update(self.render())
            except requests.exceptions.RequestException as e:
                self.update(f"Error fetching data: {e}")

        def render(self) -> str:
            """Render the display."""
            if self.eth_price is None or self.current_time is None:
                return "Loading..."
            return (
                f"{self.current_time.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"Ethereum: ${self.eth_price:,.2f}"
            )

except ImportError:
    # Don't exit immediately, allow the CLI version to run
    TEXTUAL_INSTALLED = False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="System Monitoring CLI - Track crypto prices, network status, and weather",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="""Examples:
  Basic crypto price:  python show_time.py crypto
  TUI mode:            python show_time.py crypto --textual
  Weather report:      python show_time.py weather
  Network test:        python show_time.py ping""",
    )
    subparsers = parser.add_subparsers(dest="command", required=True, metavar="COMMAND")
    # Crypto command
    crypto_parser = subparsers.add_parser(
        "crypto",
        help="Cryptocurrency price monitoring",
        description="Track Ethereum price in USD",
    )
    crypto_parser.add_argument(
        "--textual",
        action="store_true",
        help="Start Textual TUI interface (requires textual installed)",
    )

    # Weather command
    weather_parser = subparsers.add_parser(
        "weather",
        help="Local weather information",
        description="Get current weather conditions using OpenWeatherMap API",
    )

    # Ping command
    ping_parser = subparsers.add_parser(
        "ping",
        help="Network connectivity test",
        description="Measure network jitter and packet loss",
    )
    ping_parser.add_argument(
        "--host",
        default="8.8.8.8",
        help="Target host to ping (default: 8.8.8.8)",
    )

    args = parser.parse_args()

    # Handle ping command separately
    if args.command == "ping":
        from ping_jitter import main as ping_main

        ping_main(host=args.host)  # Pass host argument to ping_jitter
        sys.exit(0)

    # Handle crypto command
    if args.command == "crypto":
        if args.textual and not TEXTUAL_INSTALLED:
            sys.stderr.write(
                "Textual is not installed. Please install it "
                "to run the Textual interface.\n"
            )
            sys.exit(1)
        if args.textual:
            app = CryptoApp()
            app.run()
            return

    console = Console()

    if args.command == "weather":
            # Weather display logic
            api_key = os.getenv("OPENWEATHER_API_KEY")
            if not api_key:
                sys.stderr.write(
                    "Error: OPENWEATHER_API_KEY environment variable not set\n"
                )
                sys.exit(1)

            location = get_current_location()
            weather = get_weather(
                owm_api_key=api_key, lat=location["lat"], lon=location["lon"]
            )

            table = Table(show_header=True, header_style="bold cyan")
            table.add_column("Metric", style="dim", width=20)
            table.add_column("Value", justify="right")

            table.add_row("Time", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            table.add_row(
                "Location",
                f"{location.get('city', 'Unknown')}, "
                f"{location.get('country_name', 'Unknown')}",
            )
            table.add_row("Temperature", f"{weather['main']['temp']}°C")
            table.add_row("Conditions", weather["weather"][0]["description"].title())
            table.add_row("Humidity", f"{weather['main']['humidity']}%")
            table.add_row("Wind Speed", f"{weather['wind']['speed']} m/s")
    elif args.command == "crypto":
        # Crypto CLI display
            table = Table(show_header=True, header_style="bold magenta")
            table.add_column("Time", style="dim", width=20)
            table.add_column("Asset", width=12)
            table.add_column("Price", justify="right")

            try:
                response = requests.get(
                    "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd",
                    timeout=10,
                )
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                console.print(f"Error fetching data: {e}", style="red")
                sys.exit(1)
            data = response.json()
            eth_price = data["ethereum"]["usd"]

            table.add_row(
                now.strftime("%Y-%m-%d %H:%M:%S"), "Ethereum", f"${eth_price:,.2f}"
            )

    console.print(table)

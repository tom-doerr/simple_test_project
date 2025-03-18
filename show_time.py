"""Display current time and Ethereum price.

This module provides both a command-line interface and a Textual GUI 
to display cryptocurrency prices and current time.
"""

import argparse
import datetime
import sys
import requests

from rich.console import Console
from rich.table import Table

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
        description="Display current time and Ethereum price."
    )
    parser.add_argument(
        "--textual", action="store_true", help="Run the Textual interface."
    )
    args = parser.parse_args()

    if args.textual and not TEXTUAL_INSTALLED:
        print(
            "Textual is not installed. Please install it to run the Textual interface."
        )
        sys.exit(1)
    if args.textual:
        app = CryptoApp()
        app.run()
    else:
        # CLI version works without textual
        console = Console()

        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Time", style="dim", width=20)
        table.add_column("Asset", width=12)
        table.add_column("Price", justify="right")

        try:
            response = requests.get(
                "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd",
                timeout=10,
            )
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        except requests.exceptions.RequestException as e:
            console.print(f"Error fetching data: {e}", style="red")
            sys.exit(1)
        data = response.json()
        eth_price = data["ethereum"]["usd"]

        table.add_row(
            now.strftime("%Y-%m-%d %H:%M:%S"), "Ethereum", f"${eth_price:,.2f}"
        )
        console.print(table)

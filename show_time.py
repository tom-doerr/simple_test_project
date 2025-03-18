"""Display current time and Ethereum price."""

import argparse
import datetime
import sys
import requests

from rich.console import Console
from rich.table import Table

now = datetime.datetime.now()

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static


class CryptoApp(App):
    """A Textual app to display crypto prices."""

    CSS_PATH = "crypto.tcss"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield CryptoDisplay()
        yield Footer()


class CryptoDisplay(Static):
    """A widget to display the crypto price."""

    def on_mount(self) -> None:
        """Set a timer to refresh the crypto price every 60 seconds."""
        self.update_price()
        self.set_interval(60, self.update_price)

    def update_price(self) -> None:
        """Fetch the latest Ethereum price and update the display."""
        try:
            response = requests.get(
                "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd",
                timeout=10,
            )
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
            data = response.json()
            eth_price = data["ethereum"]["usd"]
            now = datetime.datetime.now()
            self.update(
                f"{now.strftime('%Y-%m-%d %H:%M:%S')}\nEthereum: ${eth_price:,.2f}"
            )
        except requests.exceptions.RequestException as e:
            self.update(f"Error fetching data: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Display current time and Ethereum price.")
    parser.add_argument(
        "--textual", action="store_true", help="Run the Textual interface."
    )
    args = parser.parse_args()

    if args.textual:
        app = CryptoApp()
        app.run()
    else:
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

        table.add_row(now.strftime("%Y-%m-%d %H:%M:%S"), "Ethereum", f"${eth_price:,.2f}")
        console.print(table)

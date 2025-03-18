"""Display current time and Ethereum price."""

import datetime
import sys
import requests
from rich.console import Console
from rich.table import Table

now = datetime.datetime.now()

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

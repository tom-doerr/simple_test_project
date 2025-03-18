"""Display current time and Ethereum price."""

import datetime
import requests
from rich.console import Console
from rich.table import Table

now = datetime.datetime.now()

console = Console()

table = Table(show_header=True, header_style="bold magenta")
table.add_column("Time", style="dim", width=20)
table.add_column("Asset", width=12)
table.add_column("Price", justify="right")

response = requests.get(
    "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd",
    timeout=10,
)
data = response.json()
eth_price = data["ethereum"]["usd"]

table.add_row(now.strftime("%Y-%m-%d %H:%M:%S"), "Ethereum", f"${eth_price:,.2f}")
console.print(table)

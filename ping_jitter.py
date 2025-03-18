"""Measure ping jitter to a New York server."""

import subprocess
import re
import statistics
from typing import List, Optional, Tuple
from rich.console import Console
from rich.table import Table


def parse_ping(output: str) -> List[float]:
    """Extract ping times from ping command output.

    Args:
        output: Raw output from ping command

    Returns:
        List of ping times in milliseconds
    """
    pattern = r"time=(\d+\.?\d*) ms"
    return [float(match) for match in re.findall(pattern, output)]


def calculate_jitter(times: List[float]) -> Optional[Tuple[float, float]]:
    """Calculate jitter statistics from ping times.

    Args:
        times: List of ping times in milliseconds

    Returns:
        Tuple of (average jitter, standard deviation) or None if insufficient data
    """
    if len(times) < 2:
        return None

    diffs = [abs(times[i] - times[i - 1]) for i in range(1, len(times))]
    return statistics.mean(diffs), statistics.stdev(diffs)


def main() -> None:
    """Main function to measure and display ping jitter.
    
    Args:
        None
        
    Returns:
        None
        
    Raises:
        SubprocessError: If ping command fails
        KeyboardInterrupt: Cleanly handle user cancellation
    """
    console = Console()
    host = "newyork.example.com"  # Production NY server

    try:
        # Send 4 pings with 1 second interval and 2 second timeout
        output = subprocess.check_output(
            ["ping", "-c", "4", "-i", "1", "-W", "2", host],
            stderr=subprocess.STDOUT,
            universal_newlines=True,
        )

        ping_times = parse_ping(output)
        if not ping_times:
            console.print(f"[red]Error:[/red] No ping responses from {host}")
            return

        jitter_stats = calculate_jitter(ping_times)

        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Metric", style="dim", width=20)
        table.add_column("Value", justify="right")

        table.add_row("Packets Sent", "4")
        table.add_row("Responses Received", str(len(ping_times)))
        table.add_row("Average Time (ms)", f"{statistics.mean(ping_times):.2f}")

        if jitter_stats:
            table.add_row("Jitter (avg)", f"{jitter_stats[0]:.2f} ms")
            table.add_row("Jitter (stdev)", f"{jitter_stats[1]:.2f} ms")

        console.print(table)

    except subprocess.CalledProcessError as e:
        console.print(f"[red]Error:[/red] Ping failed with exit code {e.returncode}")
        console.print(f"Output: {e.output}")
    except KeyboardInterrupt:
        console.print("\n[yellow]Test interrupted by user[/yellow]")
    except (requests.exceptions.RequestException, ValueError) as e:
        console.print(f"[red]Unexpected error:[/red] {str(e)}")


if __name__ == "__main__":
    main()

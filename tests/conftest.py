"""Configuration for pytest."""

import importlib.util
import sys

# Check if textual is installed
TEXTUAL_INSTALLED = importlib.util.find_spec("textual") is not None

# If textual is installed, import the necessary classes
if TEXTUAL_INSTALLED:
    from textual.app import App
    from textual.widgets import Static
    from textual_pytest import AppTester
    # Import the CryptoApp and CryptoDisplay from show_time.py
    sys.path.insert(0, ".")
    from show_time import CryptoApp, CryptoDisplay
else:
    # Define placeholders if textual is not installed
    App = None
    Static = None
    AppTester = None
    CryptoApp = None
    CryptoDisplay = None

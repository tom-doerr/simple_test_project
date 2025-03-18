"""Configuration for pytest."""

import importlib.util
import sys

# Check if textual is installed
TEXTUAL_INSTALLED = importlib.util.find_spec("textual") is not None

# If textual is installed, make imports available
if TEXTUAL_INSTALLED:
    try:
        # Add the current directory to the path to find show_time.py
        sys.path.insert(0, ".")
        
        # Try to import textual_pytest
        import textual_pytest
        from show_time import CryptoApp, CryptoDisplay
        
        # Make these available for tests
        app_tester = textual_pytest.AppTester
        crypto_app = CryptoApp
        crypto_display = CryptoDisplay
    except ImportError:
        # If imports fail, set TEXTUAL_INSTALLED to False
        TEXTUAL_INSTALLED = False
        app_tester = None
        crypto_app = None
        crypto_display = None
else:
    # Define placeholders if textual is not installed
    app_tester = None
    crypto_app = None
    crypto_display = None

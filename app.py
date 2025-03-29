"""
Deprecated: Use llamastyles.app instead.

This module is a compatibility wrapper that forwards to the llamastyles package.
It will be removed in a future version.
"""

import sys
import warnings

warnings.warn(
    "Direct use of app.py is deprecated. Please use 'from llamastyles.app import LlamaStylesApp' instead.",
    DeprecationWarning,
    stacklevel=2
)

from llamastyles.app import LlamaStylesApp  # noqa: E402

# For backwards compatibility
StyleGenApp = LlamaStylesApp

if __name__ == "__main__":
    print("This module is deprecated. Please use the llamastyles package directly.")
    sys.exit(1)

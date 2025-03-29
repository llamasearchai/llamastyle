"""
Deprecated: Use llamastyles.cli instead.

This module is a compatibility wrapper that forwards to the llamastyles package.
It will be removed in a future version.

See MIGRATION.md for details on how to update your code.
"""

import sys
import warnings

warnings.warn(
    "Direct use of cli.py is deprecated. Please use 'from llamastyles.cli import main' instead. See MIGRATION.md for migration instructions.",
    DeprecationWarning,
    stacklevel=2
)

# Import from the new package
from llamastyles.cli import main, LlamaStylesApp  # noqa: E402

# For backwards compatibility
StyleGenApp = LlamaStylesApp

if __name__ == "__main__":
    print("This module is deprecated. Please use the llamastyles package directly.")
    print("See MIGRATION.md for migration instructions.")
    sys.exit(main()) 
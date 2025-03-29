"""
Deprecated: Use llamastyles package directly instead.

This module is a compatibility wrapper that forwards to the llamastyles package.
It will be removed in a future version.

See MIGRATION.md for details on how to update your code.
"""

import sys
import warnings

warnings.warn(
    "Direct imports from the root package are deprecated. Please use 'import llamastyles' instead. See MIGRATION.md for migration instructions.",
    DeprecationWarning,
    stacklevel=2
)

# Re-export llamastyles package contents for backward compatibility
from llamastyles import (
    StyleTransferModel,
    ClassicStyleTransfer,
    DiffusionStyleTransfer,
    LlamaStylesApp,
    LlamaStylesConfig,
    __version__,
    logger,
)

# Backwards compatibility aliases
from llamastyles import (
    LlamaStylesApp as StyleGenApp,
)

# Re-export all public objects for backward compatibility
__all__ = [
    "StyleTransferModel",
    "ClassicStyleTransfer",
    "DiffusionStyleTransfer",
    "LlamaStylesApp",
    "StyleGenApp",  # Backwards compatibility
    "LlamaStylesConfig",
    "__version__",
    "logger",
]

if __name__ == "__main__":
    print("This module is deprecated. Please use the llamastyles package directly.")
    print("See MIGRATION.md for migration instructions.")
    sys.exit(1)

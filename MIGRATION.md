# Migrating from StyleGen to LlamaStyles

This document provides guidance on migrating from the old StyleGen package to the new LlamaStyles package.

## Overview of Changes

StyleGen has been renamed to LlamaStyles to better align with our branding. The core functionality remains the same, but there are changes to imports, command-line usage, and configuration.

## Key Changes

- Package name change: `stylegen` → `llamastyles`
- Command-line tool: `stylegen.py` → `llamastyles`
- Import paths: `from stylegen import X` → `from llamastyles import X`
- Configuration file: Updated structure and new options

## Installation Update

If you had StyleGen installed:

```bash
# Remove the old package
pip uninstall stylegen

# Install the new package
pip install llamastyles
```

Or install directly from the repository:

```bash
git clone https://github.com/yourusername/llamastyles.git
cd llamastyles
pip install -e ".[diffusion]"
```

## Import Changes

Update your import statements as follows:

```python
# Old imports
from stylegen import StyleTransferModel, ClassicStyleTransfer, StyleGenApp
from stylegen.models import DiffusionStyleTransfer
from stylegen.processing import VideoProcessor

# New imports
from llamastyles import StyleTransferModel, ClassicStyleTransfer, LlamaStylesApp
from llamastyles.models import DiffusionStyleTransfer
from llamastyles.processing import VideoProcessor
```

## API Changes

The `StyleGenApp` class has been renamed to `LlamaStylesApp`, but maintains the same interface:

```python
# Old code
from stylegen import StyleGenApp
app = StyleGenApp()
app.process_image(content="input.jpg", style="style.jpg", output="output.png")

# New code
from llamastyles import LlamaStylesApp
app = LlamaStylesApp()
app.process_image(content="input.jpg", style="style.jpg", output="output.png")
```

## Command-Line Usage

Update your command-line calls:

```bash
# Old
python stylegen.py image --content input.jpg --style style.jpg --output output.png

# New
llamastyles image --content input.jpg --style style.jpg --output output.png
# or
python -m llamastyles.cli image --content input.jpg --style style.jpg --output output.png
```

## Configuration Files

If you were using a custom configuration file with StyleGen, update the file structure to match the new format:

```yaml
# Old format
stylegen:
  model: "diffusion"
  style_strength: 0.75

# New format
llamastyles:
  model: "diffusion"
  style_strength: 0.75
```

## Backward Compatibility

For backward compatibility, we provide temporary adapter modules in the root directory. These will import from the new package structure but maintain the old API. This allows for a smoother transition, but these adapters will be removed in a future version.

## Need Help?

If you encounter any issues during migration, please:

1. Check our [documentation](https://yourusername.github.io/llamastyles)
2. Open an issue on [GitHub](https://github.com/yourusername/llamastyles/issues)

Thank you for upgrading to LlamaStyles! 🦙✨ 
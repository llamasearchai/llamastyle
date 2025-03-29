# Installing Llama-StyleGen 🦙

This document provides detailed installation instructions for Llama-StyleGen, the advanced neural style transfer package with a colorful llama-themed interface.

## Installation Options

### Option 1: Install from PyPI (Recommended)

The simplest way to install Llama-StyleGen is from PyPI:

```bash
pip install llama-stylegen
```

For additional features, you can install optional dependencies:

```bash
# For diffusion model support
pip install "llama-stylegen[diffusion]"

# For all features
pip install "llama-stylegen[diffusion,color,llm]"

# For developers
pip install "llama-stylegen[diffusion,color,llm,dev]"
```

### Option 2: Install from Source

Clone the repository and install from source:

```bash
git clone https://github.com/yourusername/llama-stylegen.git
cd llama-stylegen
pip install -e ".[diffusion,color,llm,dev]"
```

## Verifying Installation

To verify your installation, run the included verification script:

```bash
python verify_installation.py
```

Or try running the command directly:

```bash
llama-stylegen --version
```

## Running Llama-StyleGen

After installation, you can run Llama-StyleGen using the command-line interface:

```bash
# Interactive mode
llama-stylegen interactive

# Process an image
llama-stylegen image --content path/to/content.jpg --style path/to/style.jpg --output output.png

# Process a video
llama-stylegen video --content path/to/video.mp4 --style path/to/style.jpg --output output.mp4
```

## System Requirements

- **Python Version**: 3.8 or higher
- **Operating Systems**: Windows, macOS, Linux
- **Hardware Requirements**:
  - CPU: Any modern multi-core processor
  - RAM: 8GB minimum, 16GB recommended
  - GPU: Optional but recommended for faster processing
    - NVIDIA GPU with CUDA support for best performance
    - Apple Silicon (M1/M2) for acceleration on newer Macs

## GPU Setup

### NVIDIA GPUs

For NVIDIA GPUs, ensure you have the appropriate CUDA drivers installed. Llama-StyleGen will automatically detect and use your CUDA-compatible GPU if available.

To check if your CUDA setup is recognized:

```bash
python -c "import torch; print('CUDA available:', torch.cuda.is_available())"
```

### Apple Silicon (M1/M2)

On Apple Silicon Macs, Llama-StyleGen can leverage the MPS (Metal Performance Shaders) backend for acceleration:

```bash
python -c "import torch; print('MPS available:', hasattr(torch.backends, 'mps') and torch.backends.mps.is_available())"
```

## Troubleshooting

- **Missing Dependencies**: If you encounter import errors, try installing with all optional dependencies:
  ```bash
  pip install "llama-stylegen[diffusion,color,llm]"
  ```

- **Command Not Found**: If the `llama-stylegen` command is not found, ensure your Python scripts directory is in your PATH.

- **CUDA Issues**: For CUDA-related errors, make sure your NVIDIA drivers and CUDA toolkit are properly installed.

- **Out of Memory Errors**: Try processing smaller images or videos, or use the `--resolution` flag to resize inputs.

## Docker Installation

Llama-StyleGen also provides a Docker image for containerized usage:

```bash
# Build the Docker image
docker build -t llama-stylegen .

# Run in interactive mode
docker run -it --gpus all -v $(pwd)/samples:/app/samples llama-stylegen
```

## Need Help?

If you encounter any installation issues:

1. Check the [Troubleshooting](#troubleshooting) section above
2. Read the [QUICK_START.md](QUICK_START.md) guide
3. Open an issue on the [GitHub repository](https://github.com/yourusername/llama-stylegen/issues)

🦙 Happy Style Transferring with Llama-StyleGen! 🦙 
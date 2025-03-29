# Use a Python base image with CUDA support
FROM pytorch/pytorch:2.0.0-cuda11.7-cudnn8-runtime

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    ffmpeg \
    libsm6 \
    libxext6 \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Copy only requirements first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the package source code
COPY . .

# Create necessary directories
RUN mkdir -p samples/content samples/styles samples/output

# Install the package in development mode
RUN pip install -e .

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    CUDA_VISIBLE_DEVICES=0

# Create a non-root user
RUN useradd -m llama
RUN chown -R llama:llama /app
USER llama

# Set colorful llama ASCII art as entrypoint
ENTRYPOINT ["python", "-c", "from llama_stylegen.utils.ui import get_llama_ascii_art; from rich.console import Console; Console().print(get_llama_ascii_art()); import sys; sys.exit(0)"]

# Default command to run when starting the container
CMD ["llama-stylegen", "interactive"]

# Usage instructions:
# Build: docker build -t llama-stylegen .
# 
# Run interactive mode:
# docker run -it --gpus all -v $(pwd)/samples:/app/samples llama-stylegen
# 
# Process an image:
# docker run -it --gpus all -v $(pwd)/samples:/app/samples llama-stylegen llama-stylegen image --content samples/content/myimage.jpg --style samples/styles/mystyle.jpg --output samples/output/result.png
# 
# Process a video:
# docker run -it --gpus all -v $(pwd)/samples:/app/samples llama-stylegen llama-stylegen video --content samples/content/myvideo.mp4 --style samples/styles/mystyle.jpg --output samples/output/result.mp4 
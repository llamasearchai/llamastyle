# StyleGen Quick Start Guide

This guide will help you get up and running with StyleGen quickly. Follow these steps to start transforming your images and videos with AI-powered style transfer.

## Setup in 5 Minutes

1. **Clone and Setup**:
   ```bash
   git clone https://github.com/yourusername/stylegen.git
   cd stylegen
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Download Sample Content**:
   ```bash
   ./download_samples.py
   ```
   This downloads sample content and style images to get you started.

3. **Run the Example Script**:
   ```bash
   ./example-script.sh
   ```
   This applies both classic and diffusion style transfer to a sample image, and processes a short video clip.

## Common Commands

### Interactive Mode
```bash
./stylegen.py interactive
```
The easiest way to get started. Guides you through all options step by step.

### Process a Single Image
```bash
./stylegen.py image --content samples/content/content_landscape.jpg --style samples/styles/style_starry_night.jpg --output output.png
```

### Process a Video (first 30 frames)
```bash
./stylegen.py video --content samples/content/sample_video.mp4 --style samples/styles/style_kandinsky.jpg --output output.mp4 --frames 30
```

## Troubleshooting

### Installation Issues

**PyTorch Installation Problems**:
- If PyTorch installation fails, visit the [PyTorch website](https://pytorch.org/get-started/locally/) to get the correct installation command for your system.
- Apple Silicon (M1/M2) users should use: `pip install torch torchvision torchaudio`

**Diffusers/Transformers Issues**:
- If you encounter errors with Hugging Face libraries, try: `pip install --upgrade diffusers transformers`
- For token errors: Create a Hugging Face account and run `huggingface-cli login`

### Runtime Issues

**Out of Memory Errors**:
- Reduce resolution: `--resolution 512x384`
- Process fewer frames: `--frames 10`
- For image processing, try the classic model which uses less memory: `--model classic`

**Slow Processing**:
- GPU acceleration is recommended for faster processing
- For videos, start with just a few frames to test: `--frames 10`
- The classic model is generally faster than the diffusion model

**CUDA/GPU Issues**:
- If you have CUDA installed but StyleGen isn't using it, check that your PyTorch installation includes CUDA support
- Run `python -c "import torch; print(torch.cuda.is_available())"` to verify CUDA availability

**MacOS Specific Issues**:
- If you're using an M1/M2 Mac, ensure you've installed the correct version of PyTorch
- MacOS users should use the MPS device when available for hardware acceleration

## Advanced Usage

### Fine-tuning the Style Transfer

**Classic Model Parameters**:
```bash
./stylegen.py image --content my_photo.jpg --style art.jpg --output result.png --model classic --content-weight 1.0 --style-weight 1000000.0
```

**Diffusion Model with Text Prompt**:
```bash
./stylegen.py image --content my_photo.jpg --style art.jpg --output result.png --strength 0.9 --prompt "in the style of cubism with geometric patterns"
```

### Batch Processing

To process multiple images at once, you can create a simple batch script:

```bash
#!/bin/bash
for img in images/*.jpg; do
  filename=$(basename -- "$img")
  ./stylegen.py image --content "$img" --style style.jpg --output "outputs/${filename%.*}_styled.png"
done
```

## Getting Help

If you encounter issues not covered in this guide:

1. Check the logs for specific error messages
2. Ensure all dependencies are correctly installed
3. Try running with the `--verbose` flag for more detailed output
4. Search for the error message online, especially in PyTorch and Hugging Face forums
5. Report the issue on GitHub with a detailed description and logs 
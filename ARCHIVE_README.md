# StyleGen: Advanced AI Video Style Transfer CLI (ARCHIVED)

**NOTE**: This is the archived README for the old StyleGen project. The project has been renamed to LlamaStyles.
Please refer to the current README.md for updated documentation and MIGRATION.md for migration instructions.

![StyleGen Banner](https://raw.githubusercontent.com/yourusername/stylegen/main/assets/banner.png)

**StyleGen** is a powerful command-line tool for applying artistic style transfer to images and videos using state-of-the-art AI models. This project showcases advanced techniques in computer vision, generative AI, and human-computer interaction.

## 🌟 Features

- **Dual Style Transfer Engines**: Choose between classic neural style transfer or cutting-edge diffusion models
- **Video Processing**: Apply style transfer to entire videos with temporal consistency
- **Interactive Mode**: User-friendly guided interface for those unfamiliar with command-line options
- **Controllable Style Transfer**: Adjust style strength and customize with textual prompts
- **Rich Visual Feedback**: Beautiful terminal UI with progress indicators and visual comparisons
- **High-Performance Processing**: GPU acceleration with CUDA and Apple Silicon MPS support

## 🚀 Installation

### Prerequisites

- Python 3.8+
- CUDA-compatible GPU (recommended for faster processing)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/stylegen.git
   cd stylegen
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Make the script executable (Linux/Mac):
   ```bash
   chmod +x stylegen.py
   ```

## 📖 Usage

### Interactive Mode

The easiest way to use StyleGen is through the interactive mode:

```bash
python stylegen.py interactive
```

This will guide you through the style transfer process step by step.

### Command-Line Usage

#### Image Style Transfer

```bash
python stylegen.py image --content path/to/content.jpg --style path/to/style.jpg --output output.png
```

Options:
- `--model`, `-m`: Choose style transfer model (`classic` or `diffusion`, default: `diffusion`)
- `--strength`, `-st`: Style strength for diffusion model (0.1-1.0, default: 0.75)
- `--prompt`, `-p`: Text prompt for diffusion model (optional)
- `--display`, `-d`: Display comparison after processing

#### Video Style Transfer

```bash
python stylegen.py video --content path/to/video.mp4 --style path/to/style.jpg --output styled_video.mp4
```

Options:
- `--model`, `-m`: Choose style transfer model (`classic` or `diffusion`, default: `diffusion`)
- `--strength`, `-st`: Style strength for diffusion model (0.1-1.0, default: 0.75)
- `--prompt`, `-p`: Text prompt for diffusion model (optional)
- `--fps`: Output video FPS (default: same as input)
- `--resolution`, `-r`: Output video resolution as WIDTHxHEIGHT (e.g., 640x480)
- `--frames`, `-f`: Maximum number of frames to process

### Examples

1. Apply a Van Gogh style to an image using the diffusion model:
   ```bash
   python stylegen.py image --content my_photo.jpg --style starry_night.jpg --output vangogh_style.png --model diffusion --strength 0.8 --prompt "in the style of Van Gogh's Starry Night"
   ```

2. Process the first 100 frames of a video with classical style transfer:
   ```bash
   python stylegen.py video --content input_video.mp4 --style mondrian.jpg --output mondrian_video.mp4 --model classic --frames 100
   ```

## 🔬 Technical Details

### Style Transfer Models

#### Classic Neural Style Transfer

The classic implementation follows the approach introduced by Gatys et al., using features extracted from a pre-trained VGG19 network to optimize a new image that combines the content of one image with the style of another. This approach:

- Extracts feature representations for content and style using different layers of VGG19
- Computes Gram matrices of the feature maps to capture style information
- Uses L-BFGS optimization to iteratively refine the stylized image

#### Diffusion-Based Style Transfer

The diffusion model approach leverages the capabilities of Stable Diffusion with ControlNet to create a more controllable style transfer that produces high-quality results. This approach:

- Uses ControlNet with Canny edge detection to preserve the structural content
- Integrates style information through conditioning and guidance mechanisms
- Balances content preservation and style application through adjustable parameters
- Supports text prompts for fine-grained control over the stylization process

## 📊 Performance Considerations

- **GPU Acceleration**: Processing is significantly faster with CUDA-compatible GPUs
- **Memory Usage**: Diffusion models require more memory than classic methods
- **Processing Time**: Video processing can be time-intensive; consider using frame limits for testing
- **Resolution Impact**: Higher resolutions increase memory usage and processing time

## 🛣️ Roadmap

- [ ] Add support for multiple style images with regional control
- [ ] Implement batch processing for multiple images/videos
- [ ] Enhance temporal consistency in video processing
- [ ] Create a web UI for browser-based usage
- [ ] Support for real-time webcam style transfer

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Stable Diffusion](https://github.com/CompVis/stable-diffusion) for the diffusion model implementation
- [ControlNet](https://github.com/lllyasviel/ControlNet) for structural control capabilities
- [Neural Style Transfer paper](https://arxiv.org/abs/1508.06576) by Gatys et al.
- [Rich](https://github.com/Textualize/rich) for the beautiful terminal interface

---

Created by [Your Name] - Submit issues and suggestions on [GitHub](https://github.com/yourusername/stylegen/issues) 
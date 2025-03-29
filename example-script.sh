#!/bin/bash
# LlamaStyles Example Script
# This script demonstrates various features of LlamaStyles

set -e  # Exit on error

# Colors for better output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if samples directory exists
if [ ! -d "samples" ]; then
    echo -e "${YELLOW}Samples directory not found. Downloading samples...${NC}"
    python download_samples.py
fi

# Path variables
CONTENT_DIR="samples/content"
STYLE_DIR="samples/styles"
OUTPUT_DIR="samples/output"

# Create output directory if it doesn't exist
mkdir -p $OUTPUT_DIR

echo -e "${BLUE}==============================================${NC}"
echo -e "${BLUE}🦙 LlamaStyles - Example Script 🦙${NC}"
echo -e "${BLUE}==============================================${NC}"

# Function to run a command with a description
run_example() {
    description=$1
    command=$2
    
    echo -e "\n${YELLOW}$description${NC}"
    echo -e "Command: ${BLUE}$command${NC}\n"
    eval $command
    echo -e "${GREEN}✓ Example completed successfully${NC}"
    echo -e "${BLUE}----------------------------------------------${NC}"
}

# Image examples
echo -e "\n${GREEN}PART 1: Image Style Transfer Examples${NC}\n"

# Example 1: Classic neural style transfer
run_example "Example 1: Classic neural style transfer" \
    "python -m llamastyles.cli image --content $CONTENT_DIR/landscape.jpg --style $STYLE_DIR/starry_night.jpg --output $OUTPUT_DIR/classic_landscape.png --model classic"

# Example 2: Diffusion style transfer with a prompt
run_example "Example 2: Diffusion style transfer with a prompt" \
    "python -m llamastyles.cli image --content $CONTENT_DIR/portrait.jpg --style $STYLE_DIR/picasso.jpg --output $OUTPUT_DIR/diffusion_portrait.png --model diffusion --strength 0.8 --prompt 'in the style of Picasso's abstract cubism'"

# Example 3: Adjusting style strength
run_example "Example 3: Adjusting style strength (lower value = more content preservation)" \
    "python -m llamastyles.cli image --content $CONTENT_DIR/city.jpg --style $STYLE_DIR/wave.jpg --output $OUTPUT_DIR/subtle_style.png --model diffusion --strength 0.6"

# Video examples
echo -e "\n${GREEN}PART 2: Video Style Transfer Examples${NC}\n"

# Example 4: Video style transfer (small video clip, low resolution for speed)
run_example "Example 4: Quick video style transfer (5 frames, resized smaller for quick processing)" \
    "python -m llamastyles.cli video --content $CONTENT_DIR/short_clip.mp4 --style $STYLE_DIR/wave.jpg --output $OUTPUT_DIR/styled_video.mp4 --frames 5 --resolution 480x270"

# Example 5: Video style transfer with classic model
run_example "Example 5: Video with classic style transfer (5 frames)" \
    "python -m llamastyles.cli video --content $CONTENT_DIR/short_clip.mp4 --style $STYLE_DIR/starry_night.jpg --output $OUTPUT_DIR/classic_video.mp4 --model classic --frames 5 --resolution 480x270"

# Summary
echo -e "\n${GREEN}=== SUMMARY ===${NC}"
echo -e "All examples completed successfully! Output saved to the $OUTPUT_DIR directory.\n"
echo -e "Generated files:"
ls -la $OUTPUT_DIR
echo ""

# Open output directory
echo -e "${YELLOW}Would you like to open the output directory? (y/n)${NC}"
read -n 1 -r
echo ""
if [[ $REPLY =~ ^[Yy]$ ]]; then
    if [[ "$OSTYPE" == "darwin"* ]]; then
        open $OUTPUT_DIR
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        xdg-open $OUTPUT_DIR
    elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
        start $OUTPUT_DIR
    else
        echo "Cannot open directory automatically. Please open manually: $OUTPUT_DIR"
    fi
fi

echo -e "${BLUE}==============================================${NC}"
echo -e "${BLUE}🦙 Thank you for trying LlamaStyles! 🦙${NC}"
echo -e "${BLUE}==============================================${NC}"

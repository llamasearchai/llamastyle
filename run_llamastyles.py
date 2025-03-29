#!/usr/bin/env python3
"""
LlamaStyles Runner Script

This script configures the environment and launches the LlamaStyles application.
It handles both development and installed execution contexts.

Usage:
    ./run_llamastyles.py [arguments]
    python run_llamastyles.py [arguments]
"""

import os
import sys
import importlib
from pathlib import Path

def run_llamastyles():
    """Configure environment and run the CLI application"""
    # Add the current directory to the path to enable imports
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    if script_dir not in sys.path:
        sys.path.insert(0, script_dir)
    
    try:
        # First try to import from the package (installed mode)
        from llamastyles.cli import main
    except ImportError:
        try:
            # Then try direct import (development mode)
            from cli import main
        except ImportError:
            print("Error: Could not import LlamaStyles. Make sure you run this script from the correct directory.")
            print("If you installed the package, try running 'llamastyles' directly.")
            sys.exit(1)
    
    # Run the main CLI function with all arguments passed to this script
    sys.exit(main())

if __name__ == "__main__":
    # For colorful llama ASCII art, make sure we're in a Unicode terminal
    if os.name == 'nt':  # Windows
        os.system('chcp 65001')  # Set console to UTF-8
    
    run_llamastyles() 
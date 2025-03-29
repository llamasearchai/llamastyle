#!/usr/bin/env python3
"""
Verification script for LlamaStyles installation.

This script checks if LlamaStyles is correctly installed and
verifies that all required and optional dependencies are available.
"""

import sys
import os
import subprocess
import platform
from typing import Dict, List, Tuple
import importlib.util

from rich.console import Console
from rich.panel import Panel

console = Console()


def check_dependencies() -> Tuple[List[str], List[str]]:
    """Check all dependencies for LlamaStyles.
    
    Returns:
        Tuple containing lists of missing required and optional dependencies
    """
    required_modules = [
        "torch",
        "numpy",
        "PIL",
        "cv2",
        "rich",
    ]
    
    optional_modules = [
        "diffusers",
        "transformers",
        "skimage",
        "sklearn",
        "matplotlib",
        "colormath",
    ]
    
    missing_required = []
    missing_optional = []
    
    for module in required_modules:
        if importlib.util.find_spec(module) is None:
            missing_required.append(module)
    
    for module in optional_modules:
        if importlib.util.find_spec(module) is None:
            missing_optional.append(module)
    
    return missing_required, missing_optional


def get_system_info() -> Dict[str, str]:
    """Get system information.
    
    Returns:
        Dictionary with system information
    """
    info = {}
    
    # Python version
    info["python_version"] = sys.version.split()[0]
    
    # OS details
    info["os"] = platform.system()
    info["os_version"] = platform.version()
    
    # CUDA information if available
    try:
        import torch
        info["cuda_available"] = str(torch.cuda.is_available())
        if torch.cuda.is_available():
            info["cuda_version"] = torch.version.cuda
            info["cuda_devices"] = str(torch.cuda.device_count())
        
        # Check for MPS (Apple Silicon)
        if hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
            info["mps_available"] = "Yes"
        else:
            info["mps_available"] = "No"
    except:
        info["cuda_available"] = "Error checking CUDA"
    
    return info


def check_command_availability() -> bool:
    """Check if the llamastyles command is available.
    
    Returns:
        True if the command is available, False otherwise
    """
    try:
        result = subprocess.run(
            ["llamastyles", "--version"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False
        )
        return result.returncode == 0
    except FileNotFoundError:
        return False


def main():
    """Main verification function."""
    console.print(Panel.fit(
        "[bold cyan]LlamaStyles Installation Verification[/bold cyan]\n\n"
        "This script will check if LlamaStyles is correctly installed "
        "and verify all dependencies.",
        title="🦙 Welcome!",
        border_style="cyan"
    ))
    
    # Check system information
    console.print("\n[bold]System Information:[/bold]")
    system_info = get_system_info()
    for key, value in system_info.items():
        console.print(f"  - {key}: {value}")
    
    # Check dependencies
    console.print("\n[bold]Dependency Check:[/bold]")
    missing_required, missing_optional = check_dependencies()
    
    if missing_required:
        console.print("[bold red]❌ Missing required dependencies:[/bold red]")
        for dep in missing_required:
            console.print(f"  - {dep}")
    else:
        console.print("[bold green]✅ All required dependencies are installed[/bold green]")
    
    if missing_optional:
        console.print("[bold yellow]⚠️ Missing optional dependencies:[/bold yellow]")
        for dep in missing_optional:
            console.print(f"  - {dep}")
    else:
        console.print("[bold green]✅ All optional dependencies are installed[/bold green]")
    
    # Check if LlamaStyles is installed
    console.print("\n[bold]LlamaStyles Installation:[/bold]")
    
    try:
        import llamastyles
        try:
            console.print(f"✅ LlamaStyles v{llamastyles.__version__} is installed")
        except AttributeError:
            console.print("⚠️ LlamaStyles is installed, but version information is unavailable")
    except ImportError:
        console.print("[bold red]❌ LlamaStyles is not installed[/bold red]")
    
    # Check command availability
    console.print("\n[bold]Command Line Tool:[/bold]")
    if check_command_availability():
        console.print("✅ The 'llamastyles' command is available")
    else:
        console.print("[bold yellow]⚠️ The 'llamastyles' command is not available in your PATH[/bold yellow]")
        console.print("  You might need to:")
        console.print("  1. Make sure the installation completed successfully")
        console.print("  2. Activate your virtual environment if you're using one")
        console.print("  3. Add the installation directory to your PATH")
    
    console.print("\n[bold cyan]Verification complete![/bold cyan]")


if __name__ == "__main__":
    main() 
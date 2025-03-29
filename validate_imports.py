"""
Validation script to verify that all modules can be imported correctly.
This helps catch import errors before running the full application.
"""

import os
import sys
import importlib
from pathlib import Path

def print_status(message, success=True):
    """Print status message with color."""
    if success:
        print(f"✅ {message}")
    else:
        print(f"❌ {message}")

def validate_imports():
    """Validate that all critical modules can be imported."""
    
    modules_to_check = [
        # Core modules
        "llamastyles",
        "llamastyles.models.base",
        "llamastyles.models.classic",
        "llamastyles.models.diffusion",
        "llamastyles.processing.video",
        "llamastyles.processing.image",
        "llamastyles.utils.logging",
        "llamastyles.utils.dependencies",
        "llamastyles.llm_integration.function_calling",
        "llamastyles.cli",
        "llamastyles.app",
        
        # Alternative import paths for development
        "models.base",
        "models.classic",
        "models.diffusion",
        "processing.video",
        "processing.image",
        "utils.logging",
        "utils.dependencies",
        "llm_integration.function_calling",
        "cli",
        "app"
    ]
    
    successful = 0
    failed = 0
    
    print("\n=== Testing LlamaStyles module imports ===\n")
    
    for module_name in modules_to_check:
        try:
            # Add current directory to path for relative imports
            sys.path.insert(0, os.getcwd())
            
            # Try importing the module
            importlib.import_module(module_name)
            print_status(f"Successfully imported {module_name}")
            successful += 1
        except ImportError as e:
            print_status(f"Failed to import {module_name}: {e}", success=False)
            failed += 1
        except Exception as e:
            print_status(f"Error when importing {module_name}: {e}", success=False)
            failed += 1
    
    print(f"\nImport validation complete: {successful} successful, {failed} failed")
    
    if failed > 0:
        print("\nSome imports failed. This could be due to missing dependencies or import paths.")
        print("Consider running:\n  pip install -e .\n")
    else:
        print("\nAll imports successful! The LlamaStyles codebase structure looks good.")
    
    return failed == 0

if __name__ == "__main__":
    validate_imports() 
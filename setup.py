#!/usr/bin/env python
"""
Setup script for LlamaStyles.
"""

from setuptools import setup, find_namespace_packages

# Use setuptools to configure the package
# All configuration is in pyproject.toml
if __name__ == "__main__":
    setup(
        packages=find_namespace_packages(include=["llamastyles", "llamastyles.*"])
    ) 
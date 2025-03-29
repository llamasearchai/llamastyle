# Publishing Llama-StyleGen to PyPI

This document provides instructions for maintainers who want to publish new versions of Llama-StyleGen to PyPI.

## Prerequisites

Before publishing, make sure you have:

1. A PyPI account (and Test PyPI account for testing)
2. Necessary permissions for the `llama-stylegen` package
3. The following tools installed:
   ```bash
   pip install build twine
   ```

## Preparing for Release

1. **Update Version Number**: Edit `llama_stylegen/__init__.py` to bump the version number.

2. **Update CHANGELOG.md**: Make sure all changes are documented in the changelog.

3. **Run Tests**: Ensure all tests pass before publishing:
   ```bash
   pytest
   ```

4. **Check Package**: Verify your package is properly structured:
   ```bash
   python -m pip install -e .
   python verify_installation.py
   ```

## Building Distribution Packages

1. **Clean Build Directory**: Remove old builds:
   ```bash
   rm -rf build/ dist/ *.egg-info/
   ```

2. **Build Package**: Create source and wheel distributions:
   ```bash
   python -m build
   ```

   This will create two files in the `dist/` directory:
   - `llama-stylegen-X.Y.Z.tar.gz` (source archive)
   - `llama_stylegen-X.Y.Z-py3-none-any.whl` (wheel)

## Publishing to Test PyPI (Recommended First)

1. **Upload to Test PyPI**:
   ```bash
   python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
   ```

2. **Install from Test PyPI and Test**:
   ```bash
   pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple llama-stylegen
   ```

3. **Verify Installation Works**:
   ```bash
   python verify_installation.py
   ```

## Publishing to PyPI

Once you've confirmed everything works with Test PyPI, publish to the real PyPI:

1. **Upload to PyPI**:
   ```bash
   python -m twine upload dist/*
   ```

2. **Verify Package on PyPI**: Visit https://pypi.org/project/llama-stylegen/ to make sure your package is available.

3. **Test Installation**:
   ```bash
   pip install llama-stylegen
   python verify_installation.py
   ```

## Post-Release Steps

1. **Tag Release on GitHub**:
   ```bash
   git tag -a vX.Y.Z -m "Release vX.Y.Z"
   git push origin vX.Y.Z
   ```

2. **Create GitHub Release**: Go to the GitHub repository, create a new release from the tag, and include release notes.

3. **Announce Release**: Inform users about the new release through appropriate channels.

## Troubleshooting

- **Version Conflicts**: If you get version conflict errors, make sure your new version is higher than any previous version.

- **Invalid Classifiers**: Validate classifiers against the [list of valid classifiers](https://pypi.org/classifiers/).

- **Permission Issues**: Ensure you have the right permissions on PyPI for the package.

- **README Rendering Issues**: Verify your README renders correctly on PyPI.

## Continuous Integration

Consider setting up GitHub Actions for automatic testing and PyPI publishing. Here's a basic workflow you can add to `.github/workflows/publish.yml`:

```yaml
name: Publish to PyPI

on:
  release:
    types: [created]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.x'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install build twine
    - name: Build and publish
      env:
        TWINE_USERNAME: ${{ secrets.PYPI_USERNAME }}
        TWINE_PASSWORD: ${{ secrets.PYPI_PASSWORD }}
      run: |
        python -m build
        twine upload dist/*
```

Remember to set the `PYPI_USERNAME` and `PYPI_PASSWORD` secrets in your GitHub repository settings.

🦙 Happy publishing! 🦙 
# Contributing to LlamaStyles

Thank you for your interest in contributing to LlamaStyles! This document provides guidelines and instructions for contributing to this project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Environment](#development-environment)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Pull Request Process](#pull-request-process)
- [Documentation](#documentation)

## Code of Conduct

This project adheres to a Code of Conduct that all contributors are expected to follow. Please read [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) before contributing.

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/llamastyles.git
   cd llamastyles
   ```
3. Set up the upstream remote:
   ```bash
   git remote add upstream https://github.com/ORIGINAL-OWNER/llamastyles.git
   ```
4. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Development Environment

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. Install development dependencies:
   ```bash
   pip install -e ".[dev,diffusion]"
   ```

3. Install pre-commit hooks:
   ```bash
   pre-commit install
   ```

## Coding Standards

This project follows these coding standards:

- **PEP 8**: Follow the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide for Python code.
- **Type Hints**: Use type hints for function parameters and return values.
- **Docstrings**: Write docstrings for all functions, classes, and modules following the Google style.
- **Imports**: Organize imports in the following order:
  1. Standard library imports
  2. Related third-party imports
  3. Local application/library specific imports

We use the following tools to enforce coding standards:

- **Black**: For code formatting
- **isort**: For import sorting
- **mypy**: For type checking
- **pylint**: For linting

You can run these tools with:

```bash
# Format code
black llamastyles tests

# Sort imports
isort llamastyles tests

# Type checking
mypy llamastyles

# Linting
pylint llamastyles
```

## Testing

All new features and bug fixes should include tests. We use pytest for testing.

1. Run the test suite:
   ```bash
   python -m pytest
   ```

2. Run tests with coverage:
   ```bash
   python -m pytest --cov=llamastyles
   ```

3. Run specific tests:
   ```bash
   python -m pytest tests/test_models.py
   ```

## Pull Request Process

1. Update the README.md and documentation with details of changes if appropriate.
2. Update the CHANGELOG.md with details of changes.
3. Ensure all tests pass and code meets the coding standards.
4. Submit a pull request to the `main` branch.
5. The pull request will be reviewed by maintainers.
6. Once approved, the pull request will be merged.

## Documentation

- Update documentation for any new features or changes to existing functionality.
- Document all public functions, classes, and modules with docstrings.
- Keep the README.md up to date with any major changes.

## Adding New Models

When adding a new style transfer model:

1. Create a new file in the `llamastyles/models/` directory.
2. Implement the model as a subclass of `StyleTransferModel`.
3. Add appropriate tests in `tests/test_models.py`.
4. Update the CLI to support the new model.
5. Document the new model in the README.md.

## Adding New Processing Features

When adding new processing features:

1. Add the feature to the appropriate module in `llamastyles/processing/`.
2. Add tests for the new feature.
3. Update the CLI to expose the new feature if appropriate.
4. Document the new feature in the README.md.

---

Thank you for contributing to LlamaStyles! 
# Changelog

All notable changes to the Llama-StyleGen project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2023-03-11

### 🦙 Added - The Llama Renaissance!

- **MAJOR REBRAND**: Renamed project to "Llama-StyleGen" with a colorful llama-themed UI!
- **New PyPI Package**: Available as `llama-stylegen` on PyPI for easy installation
- **Colorful Llama Interface**: Added ASCII llama art and a vibrant color theme
- **Llama Facts**: Added interesting llama facts that display during processing
- **Enhanced Progress Tracking**: Rich progress bars with llama-themed colors
- **User Interaction**: Added llama-themed prompts and confirmation dialogs
- **Fun UI Elements**: Llama-themed tips, error messages, and colorful panels
- **Proper Package Structure**: Reorganized as a proper Python package for distribution

### Changed

- **API and CLI**: Commands are now `llama-stylegen` instead of `stylegen.py`
- **Dependencies**: Streamlined and organized with optional extras
- **Documentation**: Updated to reflect llama-themed changes
- **Project Structure**: Reorganized for better maintainability
- **Docker**: Updated Dockerfile for llama-stylegen package
- **Error Messages**: More friendly and descriptive with llama theming
- **Example Script**: Improved script with better examples and colorful output

### Fixed

- **Import Issues**: Fixed various import problems for better package functionality
- **Path Handling**: Improved handling of file paths in different contexts
- **Configuration**: Enhanced config loading with better error handling
- **Logging**: Improved logging configuration
- **Platform Compatibility**: Better cross-platform support

## [0.9.0] - 2023-02-15

### Added

- Video processing with temporal consistency
- Diffusion-based style transfer using Stable Diffusion
- Interactive CLI mode with guided user experience
- Rich terminal UI with progress tracking
- Support for textual prompts in diffusion models
- High-resolution output options
- Batch processing capabilities

### Changed

- Refactored code architecture for better maintainability
- Improved error handling and user feedback
- Enhanced documentation with examples
- Updated dependencies for better compatibility

### Fixed

- Memory leaks in video processing
- CUDA compatibility issues
- Style weight handling in classic neural style transfer

## [0.8.0] - 2023-01-10

### Added

- Initial release with classic neural style transfer
- Basic CLI functionality
- Support for image processing
- Documentation and examples

[Unreleased]: https://github.com/yourusername/stylegen/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/yourusername/stylegen/releases/tag/v1.0.0 
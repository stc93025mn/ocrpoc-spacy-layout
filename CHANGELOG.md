# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added (Unreleased)

- Initial proof of concept for PDF processing with spaCy Layout
- PDF download functionality for sample documents
- Structured JSON output with text, layout, spans, tables, and markdown
- Comprehensive test suite with pytest
- VS Code development environment configuration
- Pre-commit hooks for code quality
- GitHub Actions CI/CD pipeline
- Security scanning with Bandit
- Documentation and contribution guidelines

### Changed

- Migrated from unittest to pytest for better testing framework
- Updated folder structure to follow AI POC best practices
- Enhanced code quality with Black, Flake8, and pre-commit hooks

### Technical Details

- Core dependency: spaCy Layout for document processing
- Backend parsing: Docling for PDF structure extraction
- Table extraction: pandas DataFrames with automatic column detection
- Output format: Structured JSON with semantic spans and layout metadata

## [0.1.0] - 2025-10-15

### Added

- Initial release of PDF processing functionality
- Support for text, table, and layout extraction
- Sample PDF processing with IRS Form 1040 and W3C accessibility examples
- Basic error handling and logging
- JSON export functionality

### Dependencies

- spacy-layout==0.0.12
- spacy==3.8.7
- docling==2.57.0
- pandas==2.3.3
- requests==2.32.5

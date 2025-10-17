# Spacy-Layout PDF to AI-Structured Data POC

[![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![pytest](https://github.com/stc93025mn/ocrpoc-spacy-layout/actions/workflows/ci.yml/badge.svg)](https://github.com/stc93025mn/ocrpoc-spacy-layout/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/stc93025mn/ocrpoc-spacy-layout/branch/main/graph/badge.svg)](https://codecov.io/gh/stc93025mn/ocrpoc-spacy-layout)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

A proof of concept demonstrating the use of the `spacy-layout` library to convert PDFs into AI-ready structured data. This tool leverages spaCy's layout parsing capabilities to extract text, layout information, tables, and other structured elements from PDF documents.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Validation](#validation)
- [Architecture](#architecture)
- [Dependencies](#dependencies)
- [Security Considerations](#security-considerations)
- [Deployment](#deployment)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features

- **PDF Processing**: Converts PDFs to structured spaCy Doc objects
- **Layout Analysis**: Extracts page layouts, bounding boxes, and section types
- **Table Extraction**: Automatically detects and extracts tables as pandas DataFrames
- **Text Segmentation**: Identifies text spans with labels (e.g., title, section_header, text, table)
- **Markdown Output**: Generates clean markdown representations
- **JSON Export**: Saves processed data in structured JSON format

## Installation

### Prerequisites

- Python 3.10 or higher
- Virtual environment (recommended)

### Setup

1. Clone or download this repository
2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

The main dependency is `spacy-layout`, which automatically installs:

- spaCy
- Docling (for PDF parsing)
- pandas (for table data)
- And other required libraries

## Usage

### Basic Usage

Run the main processor script:

```bash
python src/pdf_processor.py
```

This will:

1. Download sample PDFs with complex layouts
2. Process them using spacy-layout
3. Save results to `data/processed_results.json`

### Programmatic Usage

```python
from src.pdf_processor import PDFProcessor

processor = PDFProcessor()

# Process a PDF file
result = processor.process_pdf("path/to/your/document.pdf")

# Access extracted data
print(result["text"])  # Full text content
print(result["layout"])  # Page layout information
print(result["tables"])  # Extracted tables as DataFrames
print(result["markdown"])  # Markdown representation

# Save results
processor.save_results([result], "output.json")
```

### Data Structure

The processed output includes:

- **filename**: Original PDF filename
- **text**: Complete extracted text
- **layout**: Page dimensions and metadata
- **spans**: Text segments with:
  - label (e.g., "text", "title", "section_header", "table")
  - text content
  - character positions
  - bounding box coordinates
  - page number
- **tables**: Extracted tabular data as pandas DataFrames
- **markdown**: Clean markdown representation

## Examples

### Processing a Tax Form (f1040.pdf)

The IRS Form 1040 demonstrates complex form layouts with multiple sections, checkboxes, and structured fields. The tool extracts:

- Header information and form metadata
- Section labels and field descriptions
- Layout coordinates for precise positioning
- Text spans categorized by content type

### Processing a Table-Heavy Document (table_example.pdf)

The W3C table example shows table extraction capabilities:

```json
{
  "tables": [
    {
      "data": [
        {
          "Disability Category": "Blind",
          "Participants": "5",
          "Ballots Completed": "1",
          "Results.Accuracy": "34.5%, n=1"
        }
        // ... more rows
      ]
    }
  ]
}
```

## Validation

The POC has been tested with:

- Complex forms (IRS tax forms)
- Documents with tables (accessibility examples)
- Multi-page documents
- Various fonts and layouts

### Running Tests

Run tests with coverage reporting:

```bash
# Run tests with coverage
pytest --cov --cov-branch --cov-report=xml

# Run tests (using configuration from pyproject.toml)
pytest

# Generate HTML coverage report
pytest --cov-report=html
```

### Code Coverage

This project uses [Codecov](https://codecov.io) for code coverage reporting. Coverage reports are automatically generated and uploaded to Codecov during CI/CD.

- **Coverage Requirement**: 80% minimum
- **Branch Coverage**: Enabled
- **Reports**: HTML, XML, and terminal output

[![codecov](https://codecov.io/gh/stc93025mn/ocrpoc-spacy-layout/branch/main/graph/badge.svg)](https://codecov.io/gh/stc93025mn/ocrpoc-spacy-layout)

## Architecture

```text
src/
├── pdf_processor.py    # Main processing logic
tests/
├── test_pdf_processor.py  # Unit tests
samples/
├── pdfs/               # Downloaded sample PDFs
├── processed_results.json  # Processing output
docs/                    # Documentation
```

## Dependencies

Key dependencies (see requirements.txt):

- spacy-layout: Core PDF processing
- requests: PDF downloading
- pandas: Data manipulation
- spacy: NLP framework
- docling: Document parsing

## Security Considerations

- PDFs are processed locally; no data is sent to external services
- Downloaded PDFs are cached in the `data/pdfs/` directory
- No sensitive data handling in this POC

## Deployment

### Local Development

1. Set up virtual environment
2. Install dependencies
3. Run processor on your PDFs

### Production Considerations

- For large-scale processing, use `spaCyLayout.pipe()` for batch processing
- Consider serialization with `DocBin` for caching processed documents
- Monitor memory usage for large PDFs

## Future Enhancements

- Integration with LLM pipelines for content analysis
- Support for additional document formats
- Web interface for PDF upload and processing
- Advanced table structure recognition
- Custom layout parsers for domain-specific documents

## Contributing

This is a proof of concept. For contributions:

1. Add tests for new functionality
2. Update documentation
3. Follow Python best practices

## License

This project uses the MIT License (same as spacy-layout).

## Acknowledgments

- [spaCy](https://spacy.io/) for the NLP framework
- [Docling](https://ds4sd.github.io/docling/) for document parsing
- [spaCy Layout](https://github.com/explosion/spacy-layout) for layout analysis

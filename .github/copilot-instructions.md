# AI Coding Agent Instructions for Spacy-Layout PDF Processor

## Project Architecture

This is a Python proof-of-concept using `spaCy Layout` for converting PDFs to AI-ready structured data. The core architecture centers on the `PDFProcessor` class in `src/pdf_processor.py` that:

- Downloads sample PDFs to `samples/pdfs/` directory
- Processes documents using `spaCyLayout(self.nlp)` where `nlp = spacy.blank("en")`
- Extracts structured data: text, layout metadata, semantic spans, tables as pandas DataFrames, and markdown
- Outputs JSON to `samples/processed_results.json`

**Key Data Flow:**
1. PDF → Docling parser → spaCy Doc with layout spans
2. `doc.spans["layout"]` contains semantic segments (text, title, section_header, table)
3. `doc._.tables` provides table spans with `span._.data` as pandas DataFrames
4. `doc._.markdown` generates clean markdown representation

## Critical Developer Workflows

### Environment Setup
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Core Commands
- **Process PDFs**: `python src/pdf_processor.py` (downloads samples and processes)
- **Run tests**: `python -m unittest tests.test_pdf_processor`
- **Manual processing**: `processor.process_pdf("path/to/file.pdf")`

### File Organization
- `src/pdf_processor.py`: Main `PDFProcessor` class with `process_pdf()` method
- `tests/test_pdf_processor.py`: Unit tests validating output structure
- `samples/pdfs/`: Cached PDF downloads
- `samples/processed_results.json`: Structured processing results

## Project-Specific Patterns

### PDF Processing Pattern
```python
from src.pdf_processor import PDFProcessor

processor = PDFProcessor()  # Initializes spacy.blank("en") + spaCyLayout
result = processor.process_pdf(pdf_path)

# Access extracted data
result["text"]        # Full document text
result["layout"]      # Page dimensions/metadata
result["spans"]       # List of semantic spans with labels, positions, text
result["tables"]      # List of table spans with pandas DataFrame data
result["markdown"]    # Clean markdown representation
```

### Span Structure Pattern
Each span in `result["spans"]` follows:
```python
{
    "label": "text|title|section_header|table",
    "text": "span content",
    "start|end": "token positions",
    "start_char|end_char": "character positions",
    "layout": {"x", "y", "width", "height", "page_no"},
    "heading": "associated heading text if any"
}
```

### Table Extraction Pattern
Tables are extracted as pandas DataFrames:
```python
for table_span in result["tables"]:
    if table_span["data"]:  # pandas DataFrame as dict records
        df = pd.DataFrame(table_span["data"])
        # Process tabular data
```

### Error Handling Pattern
```python
try:
    result = processor.process_pdf(pdf_path)
    print(f"Successfully processed {pdf_path}")
except Exception as e:
    print(f"Error processing {pdf_path}: {e}")
```

## Integration Points

### External Dependencies
- **spaCy Layout**: Core PDF processing (`spaCyLayout(nlp)`)
- **Docling**: Backend document parsing
- **pandas**: Table data manipulation
- **requests**: PDF downloading from URLs

### Data Formats
- **Input**: PDF files (local paths or URLs)
- **Output**: Structured JSON with consistent schema
- **Tables**: pandas DataFrames serialized as record dicts

## Development Conventions

### Code Style
- Type hints on all function signatures
- PEP 8 compliance
- Comprehensive docstrings
- Class-based organization (`PDFProcessor`)

### Testing Approach
- Unit tests in `tests/test_pdf_processor.py`
- Validate output data structure presence
- Test PDF download functionality
- Skip tests when sample files unavailable

### File Paths
- Relative paths for sample data (`samples/pdfs/`, `samples/processed_results.json`)
- Absolute paths for source imports (`from src.pdf_processor import PDFProcessor`)

## Common Patterns to Follow

### When Adding New Processing Features
1. Extend `PDFProcessor` class methods
2. Add corresponding test cases
3. Update output JSON structure if needed
4. Maintain backward compatibility

### When Processing Custom PDFs
```python
processor = PDFProcessor()
results = []

for pdf_path in pdf_files:
    try:
        result = processor.process_pdf(pdf_path)
        results.append(result)
    except Exception as e:
        print(f"Failed to process {pdf_path}: {e}")

processor.save_results(results, "output.json")
```

### When Working with Layout Data
- Always check `span._.layout` for positioning data
- Page numbers are 1-indexed
- Coordinates are in points (72 DPI)
- Use `span.label_` for content type classification

## Performance Considerations

- Large PDFs require significant memory
- Use `spaCyLayout.pipe()` for batch processing multiple documents
- Consider `DocBin` serialization for caching processed documents
- Monitor memory usage with complex layouts

## Security Notes

- PDFs processed locally with no external data transmission
- Input validation required for file paths
- Downloaded PDFs cached in project directory
- No sensitive data handling in current implementation
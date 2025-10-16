# AI Agent Documentation for Spacy-Layout POC

## Project Overview

This is a proof of concept (POC) project demonstrating PDF-to-structured-data conversion using the `spacy-layout` library. The project processes PDF documents and extracts structured information suitable for AI/ML applications, including text content, layout metadata, tables, and semantic spans.

## Architecture

### Core Components

1. **PDFProcessor Class** (`src/pdf_processor.py`)
   - Main processing logic
   - Downloads sample PDFs
   - Processes documents with spaCy Layout
   - Exports results to JSON

2. **Test Suite** (`tests/test_pdf_processor.py`)
   - Unit tests for core functionality
   - Validates PDF processing and data export

3. **Sample Data** (`samples/`)
   - Downloaded PDFs for testing
   - Processed results in JSON format

### Key Dependencies

- `spacy-layout`: Core PDF processing library
- `spacy`: NLP framework for tokenization
- `docling`: Document parsing backend
- `pandas`: Data manipulation for tables
- `requests`: HTTP client for PDF downloads

## Data Flow

1. **Input**: PDF files (local paths or URLs)
2. **Processing**:
   - Docling parses PDF to document structure
   - spaCy Layout creates Doc object with layout spans
   - Tables extracted as pandas DataFrames
   - Text and metadata collected
3. **Output**: Structured JSON with text, layout, spans, tables, markdown

## Processing Details

### Layout Spans

- **Labels**: text, title, section_header, table, etc.
- **Attributes**: bounding boxes, page numbers, headings
- **Purpose**: Semantic segmentation of document content

### Tables

- **Format**: pandas DataFrame
- **Access**: Via `doc._.tables` and `span._.data`
- **Features**: Automatic column detection, data type inference

### Layout Information

- **Pages**: Dimensions, page numbers
- **Spans**: Position coordinates, content types
- **Hierarchy**: Heading relationships

## Extension Points

### Custom Processing

- Add new span types in `process_pdf()`
- Implement custom table display functions
- Extend output formats (XML, CSV, etc.)

### Integration Points

- LLM pipelines for content analysis
- RAG systems for document chunking
- Search indexing for document retrieval

## Testing Strategy

- **Unit Tests**: Core functionality validation
- **Integration Tests**: End-to-end PDF processing
- **Sample Validation**: Real PDF processing verification

## Performance Considerations

- **Memory**: Large PDFs require significant RAM
- **CPU**: Processing is compute-intensive
- **Batch Processing**: Use `pipe()` for multiple documents
- **Caching**: Serialize processed docs with DocBin

## Future Enhancements

### Potential Features

- Web interface for PDF upload
- Support for additional document formats
- Advanced table structure recognition
- Custom layout parsers for domain-specific docs

### AI/ML Integration

- Named entity recognition on extracted text
- Document classification
- Content summarization
- Question answering over document content

## Development Guidelines

### Code Style

- Follow PEP 8 Python standards
- Use type hints for function signatures
- Comprehensive error handling
- Clear documentation strings

### Testing

- Maintain high test coverage
- Test with various PDF types
- Validate output data structures
- Performance benchmarking

### Security

- Input validation for file paths
- Safe PDF processing
- No external data transmission
- Isolated execution environment

## Troubleshooting

### Common Issues

- **Memory Errors**: Reduce batch sizes or increase memory limits
- **OCR Failures**: Check PDF quality and language settings
- **Table Detection**: Verify table structure in source PDF

### Debugging

- Enable verbose logging in Docling
- Inspect intermediate Doc objects
- Validate JSON output structure

## Deployment Notes

- Use virtual environments for isolation
- Consider containerization for portability
- Monitor resource usage in production
- Implement proper error handling and logging

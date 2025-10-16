import os
import requests
import spacy
from spacy_layout import spaCyLayout
import json
from typing import List, Dict, Any

class PDFProcessor:
    def __init__(self):
        # Initialize spaCy with blank English model
        self.nlp = spacy.blank("en")
        self.layout_processor = spaCyLayout(self.nlp)

    def download_pdf(self, url: str, filename: str) -> str:
        """Download a PDF from URL to samples/pdfs/ directory."""
        pdf_dir = "samples/pdfs"
        os.makedirs(pdf_dir, exist_ok=True)
        filepath = os.path.join(pdf_dir, filename)
        
        response = requests.get(url)
        response.raise_for_status()
        
        with open(filepath, 'wb') as f:
            f.write(response.content)
        
        return filepath

    def process_pdf(self, pdf_path: str) -> Dict[str, Any]:
        """Process a PDF and extract structured data."""
        doc = self.layout_processor(pdf_path)
        
        # Extract basic information
        result = {
            "filename": os.path.basename(pdf_path),
            "text": doc.text,
            "layout": {
                "pages": [
                    {
                        "page_no": page.page_no,
                        "width": page.width,
                        "height": page.height
                    } for page in doc._.layout.pages
                ]
            },
            "spans": [
                {
                    "label": span.label_,
                    "text": span.text,
                    "start": span.start,
                    "end": span.end,
                    "start_char": span.start_char,
                    "end_char": span.end_char,
                    "layout": {
                        "x": span._.layout.x,
                        "y": span._.layout.y,
                        "width": span._.layout.width,
                        "height": span._.layout.height,
                        "page_no": span._.layout.page_no
                    } if span._.layout else None,
                    "heading": span._.heading.text if span._.heading else None
                } for span in doc.spans["layout"]
            ],
            "tables": [
                {
                    "start": table.start,
                    "end": table.end,
                    "layout": {
                        "x": table._.layout.x,
                        "y": table._.layout.y,
                        "width": table._.layout.width,
                        "height": table._.layout.height,
                        "page_no": table._.layout.page_no
                    } if table._.layout else None,
                    "data": table._.data.to_dict('records') if table._.data is not None else None
                } for table in doc._.tables
            ],
            "markdown": doc._.markdown
        }
        
        return result

    def save_results(self, results: List[Dict[str, Any]], output_file: str):
        """Save processing results to JSON file."""
        with open(output_file, 'w') as f:
            json.dump(results, f, indent=2)

def main():
    processor = PDFProcessor()
    
    # Sample PDFs to download and process
    pdf_urls = [
        ("https://www.irs.gov/pub/irs-pdf/f1040.pdf", "f1040.pdf"),
        ("https://www.w3.org/WAI/WCAG21/working-examples/pdf-table/table.pdf", "table_example.pdf"),
        ("https://www.africau.edu/images/default/sample.pdf", "sample_text.pdf")
    ]
    
    results = []
    
    for url, filename in pdf_urls:
        try:
            print(f"Downloading {filename}...")
            pdf_path = processor.download_pdf(url, filename)
            print(f"Processing {filename}...")
            result = processor.process_pdf(pdf_path)
            results.append(result)
            print(f"Successfully processed {filename}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")
    
    # Save results
    output_file = "samples/processed_results.json"
    os.makedirs("samples", exist_ok=True)
    processor.save_results(results, output_file)
    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    main()
import unittest
import os
import json
from src.pdf_processor import PDFProcessor

class TestPDFProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = PDFProcessor()
        self.test_pdf_path = "samples/pdfs/sample_text.pdf"  # Assuming it exists from main run

    def test_pdf_processing(self):
        """Test that PDF processing returns expected structure."""
        if os.path.exists(self.test_pdf_path):
            result = self.processor.process_pdf(self.test_pdf_path)
            
            # Check basic structure
            self.assertIn("filename", result)
            self.assertIn("text", result)
            self.assertIn("layout", result)
            self.assertIn("spans", result)
            self.assertIn("tables", result)
            self.assertIn("markdown", result)
            
            # Check that text is not empty
            self.assertGreater(len(result["text"]), 0)
            
            # Check spans
            self.assertIsInstance(result["spans"], list)
            
            # Check tables
            self.assertIsInstance(result["tables"], list)
        else:
            self.skipTest("Test PDF not found")

    def test_download_pdf(self):
        """Test PDF download functionality."""
        # Test with a small PDF
        url = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
        filename = "test_download.pdf"
        filepath = self.processor.download_pdf(url, filename)
        
        self.assertTrue(os.path.exists(filepath))
        self.assertGreater(os.path.getsize(filepath), 0)
        
        # Clean up
        os.remove(filepath)

    def test_save_results(self):
        """Test saving results to JSON."""
        test_results = [{"test": "data"}]
        output_file = "test_output.json"
        
        self.processor.save_results(test_results, output_file)
        
        self.assertTrue(os.path.exists(output_file))
        
        with open(output_file, 'r') as f:
            loaded = json.load(f)
        
        self.assertEqual(loaded, test_results)
        
        # Clean up
        os.remove(output_file)

if __name__ == '__main__':
    unittest.main()
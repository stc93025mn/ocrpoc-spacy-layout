import pytest
import os
import json
from src.pdf_processor import PDFProcessor


class TestPDFProcessor:
    @pytest.fixture
    def processor(self):
        return PDFProcessor()

    @pytest.fixture
    def test_pdf_path(self):
        return "data/pdfs/sample_text.pdf"

    def test_pdf_processing(self, processor, test_pdf_path):
        """Test that PDF processing returns expected structure."""
        if not os.path.exists(test_pdf_path):
            pytest.skip("Test PDF not found")

        result = processor.process_pdf(test_pdf_path)

        # Check basic structure
        assert "filename" in result
        assert "text" in result
        assert "layout" in result
        assert "spans" in result
        assert "tables" in result
        assert "markdown" in result

        # Check that text is not empty
        assert len(result["text"]) > 0

        # Check spans
        assert isinstance(result["spans"], list)

        # Check tables
        assert isinstance(result["tables"], list)

    def test_download_pdf(self, processor):
        """Test PDF download functionality."""
        # Test with a small PDF
        url = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
        filename = "test_download.pdf"
        filepath = processor.download_pdf(url, filename)

        assert os.path.exists(filepath)
        assert os.path.getsize(filepath) > 0

        # Clean up
        os.remove(filepath)

    def test_save_results(self, processor):
        """Test saving results to JSON."""
        test_results = [{"test": "data"}]
        output_file = "test_output.json"

        processor.save_results(test_results, output_file)

        assert os.path.exists(output_file)

        with open(output_file, "r") as f:
            loaded = json.load(f)

        assert loaded == test_results

        # Clean up
        os.remove(output_file)

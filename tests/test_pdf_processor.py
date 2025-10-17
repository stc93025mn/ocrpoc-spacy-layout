import pytest
import os
import json
from unittest.mock import Mock, patch
from src.pdf_processor import PDFProcessor


class TestPDFProcessor:
    @pytest.fixture
    def processor(self):
        return PDFProcessor()

    def test_pdf_processing(self, processor):
        """Test that PDF processing returns expected structure."""
        # Mock the doc object and its attributes
        mock_doc = Mock()
        mock_doc.text = "Sample text"

        # Mock layout pages
        mock_page = Mock()
        mock_page.page_no = 1
        mock_page.width = 100
        mock_page.height = 200
        mock_doc._.layout.pages = [mock_page]

        # Mock spans
        mock_span = Mock()
        mock_span.label_ = "text"
        mock_span.text = "span text"
        mock_span.start = 0
        mock_span.end = 9
        mock_span.start_char = 0
        mock_span.end_char = 9
        mock_span._.layout = Mock()
        mock_span._.layout.x = 10
        mock_span._.layout.y = 20
        mock_span._.layout.width = 50
        mock_span._.layout.height = 10
        mock_span._.layout.page_no = 1
        mock_span._.heading = None
        mock_doc.spans = {"layout": [mock_span]}

        # Mock tables
        mock_table = Mock()
        mock_table.start = 10
        mock_table.end = 20
        mock_table._.layout = Mock()
        mock_table._.layout.x = 10
        mock_table._.layout.y = 30
        mock_table._.layout.width = 50
        mock_table._.layout.height = 20
        mock_table._.layout.page_no = 1
        mock_table._.data = Mock()
        mock_table._.data.to_dict = Mock(return_value=[{"col": "value"}])
        mock_doc._.tables = [mock_table]

        mock_doc._.markdown = "# Sample markdown"

        with patch.object(
            processor, "layout_processor", return_value=mock_doc
        ) as mock_layout:
            result = processor.process_pdf("dummy.pdf")

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
            assert len(result["spans"]) > 0

            # Check tables
            assert isinstance(result["tables"], list)
            assert len(result["tables"]) > 0

            # Verify the layout processor was called
            mock_layout.assert_called_once_with("dummy.pdf")

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

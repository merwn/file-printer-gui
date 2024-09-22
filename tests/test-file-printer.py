import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from file_printer import print_file, get_printers

class TestFilePrinter(unittest.TestCase):

    @patch('file_printer.win32print.GetDefaultPrinter')
    def test_get_printers(self, mock_get_default_printer):
        mock_get_default_printer.return_value = "Default Printer"
        printers = get_printers()
        self.assertIn("Default Printer", printers)

    @patch('file_printer.win32api.ShellExecute')
    def test_print_pdf_file(self, mock_shell_execute):
        result = print_file("test.pdf", "Test Printer")
        self.assertTrue(result)
        mock_shell_execute.assert_called_once()

    @patch('file_printer.Image.open')
    @patch('file_printer.win32print.OpenPrinter')
    @patch('file_printer.win32print.StartDoc')
    @patch('file_printer.win32print.EndDoc')
    @patch('file_printer.win32print.ClosePrinter')
    def test_print_image_file(self, mock_close_printer, mock_end_doc, mock_start_doc, mock_open_printer, mock_image_open):
        mock_image = MagicMock()
        mock_image_open.return_value = mock_image
        result = print_file("test.jpg", "Test Printer")
        self.assertTrue(result)
        mock_image_open.assert_called_once()
        mock_open_printer.assert_called_once()
        mock_start_doc.assert_called_once()
        mock_end_doc.assert_called_once()
        mock_close_printer.assert_called_once()

if __name__ == '__main__':
    unittest.main()

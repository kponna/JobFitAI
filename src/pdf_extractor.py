# src/pdf_extractor.py
import PyPDF2

class PDFExtractor:
    """Extract text from PDF files using PyPDF2."""

    def __init__(self):
        """Initialize the PDFExtractor."""
        pass

    def extract_text(self, pdf_path: str) -> str:
        """
        Extract text content from a given PDF file.

        Args:
            pdf_path (str): Path to the PDF file.

        Returns:
            str: Extracted text from the PDF.

        Raises:
            FileNotFoundError: If the file does not exist.
            Exception: For other unexpected errors.
        """
        text = ""
        try:
            with open(pdf_path, "rb") as file:
                reader = PyPDF2.PdfReader(file)
                for page in reader.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
        except FileNotFoundError:
            print(f"Error: The file '{pdf_path}' was not found.")
        except Exception as e:
            print(f"An error occurred while extracting text: {e}")
        
        return text

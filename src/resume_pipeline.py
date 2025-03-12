# src/resume_pipeline.py
from src.pdf_extractor import PDFExtractor
from src.audio_transcriber import AudioTranscriber

class ResumePipeline:
    """
    Process resume files (PDF or audio) and return extracted text.
    """

    def __init__(self):
        """Initialize the ResumePipeline with PDFExtractor and AudioTranscriber."""
        self.pdf_extractor = PDFExtractor()
        self.audio_transcriber = AudioTranscriber()

    def process_resume(self, file_path: str, file_type: str) -> str:
        """
        Process a resume file and extract text based on its type.

        Args:
            file_path (str): Path to the resume file.
            file_type (str): Type of the file ('pdf' or 'audio').

        Returns:
            str: Extracted text from the resume.

        Raises:
            ValueError: If the file type is unsupported.
            FileNotFoundError: If the specified file does not exist.
            Exception: For other unexpected errors.
        """
        try:
            file_type_lower = file_type.lower()
            if file_type_lower == "pdf":
                return self.pdf_extractor.extract_text(file_path)
            elif file_type_lower in ["audio", "wav", "mp3"]:
                return self.audio_transcriber.transcribe(file_path)
            else:
                raise ValueError("Unsupported file type. Use 'pdf' or 'audio'.")
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")
            return ""
        except ValueError as ve:
            print(f"Error: {ve}")
            return ""
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return ""

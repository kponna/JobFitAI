# src/audio_transcriber.py
import whisper

class AudioTranscriber:
    """Transcribe audio files using OpenAI Whisper."""
    def __init__(self, model_size: str = "base"):
        """
        Initializes the Whisper model for transcription.
        
        Args:
            model_size (str): The size of the Whisper model to load. Defaults to "base".
        """
        self.model_size = model_size 
        self.model = whisper.load_model(self.model_size)

    def transcribe(self, audio_path: str) -> str:
        """
        Transcribes the given audio file and returns the text.
        
        Args:
            audio_path (str): The path to the audio file to be transcribed.
        
        Returns:
            str: The transcribed text.
        
        Raises:
            Exception: If transcription fails.
        """
        try:
            result = self.model.transcribe(audio_path)
            return result["text"]
        except Exception as e:
            print(f"Error transcribing audio: {e}")
            return ""
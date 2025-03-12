# # src/analyzer.py 
 
import os
from openai import OpenAI 
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class DeepInfraAnalyzer:
    """
    Calls DeepSeek-R1 model on DeepInfra using an OpenAI-compatible interface.
    This class processes resume text and extracts structured information using AI.
    """ 
    def __init__(
        self,
        api_key: str= os.getenv("DEEPINFRA_TOKEN"),
        model_name: str = "deepseek-ai/DeepSeek-R1"
    ):
        """
        Initializes the DeepInfraAnalyzer with API key and model name.

        :param api_key: API key for authentication 
        :param model_name: The name of the model to use 
        """
        try:
            self.openai_client = OpenAI(
                api_key=api_key, 
                base_url="https://api.deepinfra.com/v1/openai",
            )
            self.model_name = model_name 
        except Exception as e:
            raise RuntimeError(f"Failed to initialize OpenAI client: {e}")
    

    def analyze_text(self, text: str) -> str:
        """
        Processes the given resume text and extracts key information in JSON format.
        The response will contain structured details about key skills, experience, education, etc.

        :param text: The resume text to analyze
        :return: JSON string with structured resume analysis
        """
        prompt = (
            "You are an AI job resume matcher assistant. "
            "DO NOT show your chain of thought. "
            "Respond ONLY in English. "
            "Extract the key skills, experiences, education, achievements, etc. from the following resume text. "
            "Then produce the final output as a well-structured JSON with a top-level key called \"analysis\". "
            "Inside \"analysis\", you can have subkeys like \"key_skills\", \"experiences\", \"education\", etc. "
            "Return ONLY the final JSON, with no extra commentary.\n\n"
            f"Resume Text:\n{text}\n\n"
            "Required Format (example):\n"
            "```\n"
            "{\n"
            "  \"analysis\": {\n"
            "    \"key_skills\": [...],\n"
            "    \"experiences\": [...],\n"
            "    \"education\": [...],\n"
            "    \"achievements\": [...],\n"
            "    ...\n"
            "  }\n"
            "}\n"
            "```\n"
        ) 
        try:
            response = self.openai_client.chat.completions.create(
                model=self.model_name,
                messages=[{"role": "user", "content": prompt}], 
            )
            return response.choices[0].message.content
        except Exception as e:
            raise RuntimeError(f"Error processing resume text: {e}") 
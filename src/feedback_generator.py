from src.analyzer import DeepInfraAnalyzer 

class FeedbackGenerator:
    """
    Generates feedback for resume improvement based on a job description 
    using the DeepInfraAnalyzer.
    """

    def __init__(self, analyzer: DeepInfraAnalyzer):
        """
        Initializes the FeedbackGenerator with an instance of DeepInfraAnalyzer.

        Args:
            analyzer (DeepInfraAnalyzer): An instance of the DeepInfraAnalyzer class.
        """
        self.analyzer = analyzer 

    def generate_feedback(self, resume_text: str, job_description: str) -> str:
        """
        Generates feedback on how well a resume aligns with a job description.

        Args:
            resume_text (str): The extracted text from the resume.
            job_description (str): The job posting or job description.

        Returns:
            str: A JSON-formatted response containing:
                - "match_score" (int): A score from 0-100 indicating job match quality.
                - "job_alignment" (dict): Categorization of strong and weak matches.
                - "missing_skills" (list): Skills missing from the resume.
                - "recommendations" (list): Actionable suggestions for improvement.

        Raises:
            Exception: If an unexpected error occurs during analysis.
        """
        try:
            prompt = (
                "You are an AI job resume matcher assistant. "
                "DO NOT show your chain of thought. "
                "Respond ONLY in English. "
                "Compare the following resume text with the job description. "
                "Calculate a match score (0-100) for how well the resume matches. "
                "Identify keywords from the job description that are missing in the resume. "
                "Provide bullet-point recommendations to improve the resume for better alignment.\n\n"
                f"Resume Text:\n{resume_text}\n\n"
                f"Job Description:\n{job_description}\n\n"
                "Return JSON ONLY in this format:\n"
                "{\n"
                "  \"job_match\": {\n"
                "    \"match_score\": <integer>,\n"
                "    \"job_alignment\": {\n"
                "      \"strong_match\": [...],\n"
                "      \"weak_match\": [...]\n"
                "    },\n"
                "    \"missing_skills\": [...],\n"
                "    \"recommendations\": [\n"
                "      \"<Actionable Suggestion 1>\",\n"
                "      \"<Actionable Suggestion 2>\",\n"
                "      ...\n"
                "    ]\n"
                "  }\n"
                "}"
            ) 
            return self.analyzer.analyze_text(prompt)

        except Exception as e:
            print(f"Error in generating feedback: {e}")
            return "{}"  # Returning an empty JSON string in case of failure

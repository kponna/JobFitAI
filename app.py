import gradio as gr 
from src.resume_pipeline import ResumePipeline
from src.analyzer import DeepInfraAnalyzer
from src.feedback_generator import FeedbackGenerator

# Pipeline for PDF/audio
resume_pipeline = ResumePipeline()

# Initialize the DeepInfra analyzer   
analyzer = DeepInfraAnalyzer()

# Feedback generator
feedback_generator = FeedbackGenerator(analyzer) 
 
def analyze_resume(resume_path, job_desc):
    """
    Gradio callback function to analyze a resume against a job description.

    Args:
        resume_path (str): Path to the uploaded resume file (PDF or audio).
        job_desc (str): The job description text for comparison.
    
    """ 
    try:
        if not resume_path or not job_desc:
            return {"error": "Please upload a resume and enter a job description."}

        # Determine file type from extension
        lower_name = resume_path.lower()
        file_type = "pdf" if lower_name.endswith(".pdf") else "audio"

        # Extract text from the resume
        resume_text = resume_pipeline.process_resume(resume_path, file_type)

        # Analyze extracted text
        analysis_result = analyzer.analyze_text(resume_text)

        # Generate feedback and recommendations
        feedback = feedback_generator.generate_feedback(resume_text, job_desc)

        # Return structured response
        return {
            "analysis": analysis_result,
            "recommendations": feedback
        }
    except ValueError as e:
        return {"error": f"Unsupported file type or processing error: {str(e)}"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {str(e)}"}
    
# Define Gradio interface
demo = gr.Interface(
    fn=analyze_resume,
    inputs=[
        gr.File(label="Resume (PDF/Audio)", type="filepath"),
        gr.Textbox(lines=5, label="Job Description"),
    ],
    outputs="json",
    title="JobFitAI: AI Resume Analyzer",
    description="""
Upload your resume/cv (PDF or audio) and paste the job description to get a match score,
missing keywords, and actionable recommendations.""",
)

if __name__ == "__main__": 
    demo.launch(server_name="0.0.0.0", server_port=8000) 
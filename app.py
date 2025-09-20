import gradio as gr
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# Chat function
def career_chatbot(user_input):
    response = model.generate_content(user_input)
    return response.text

# Gradio interface
interface = gr.Interface(
    fn=career_chatbot,
    inputs=gr.Textbox(lines=2, placeholder="Ask about careers, skills, or resources..."),
    outputs="text",
    theme="default",
    title="AI Career & Skills Advisor",
    description="Powered by Gemini. Ask me anything about your career path!"
)

interface.launch(share=True)
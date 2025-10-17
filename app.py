import gradio as gr
import google.generativeai as genai
import os
import json
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize Gemini model
model = genai.GenerativeModel("gemini-pro-latest")

# Global chat history
chat_history = []

# Career assessment questions
quiz_questions = [
    "What type of work environment do you prefer? (Remote/Office/Hybrid)",
    "Do you enjoy working with people or prefer independent work?",
    "Are you more interested in creative or analytical tasks?",
    "What's your preferred work-life balance priority?",
    "Do you prefer stable routine or dynamic, changing tasks?"
]

# Enhanced chat function with context
def career_chatbot(user_input, history):
    context = "\n".join([f"User: {h[0]}\nBot: {h[1]}" for h in history[-3:]])
    prompt = f"Context: {context}\n\nUser: {user_input}\n\nAs a career advisor, provide helpful guidance:"
    
    response = model.generate_content(prompt)
    history.append([user_input, response.text])
    return "", history

# Career assessment function
def assess_career(q1, q2, q3, q4, q5):
    if not all([q1, q2, q3, q4, q5]):
        return "Please answer all questions to get career recommendations."
    
    prompt = f"""Based on these career assessment answers:
    1. Work environment: {q1}
    2. People vs independent: {q2}
    3. Creative vs analytical: {q3}
    4. Work-life balance: {q4}
    5. Routine vs dynamic: {q5}
    
    Suggest 3 suitable career paths with brief explanations."""
    
    response = model.generate_content(prompt)
    return response.text

# Skill gap analysis
def analyze_skills(current_skills, target_role):
    prompt = f"""Current skills: {current_skills}
    Target role: {target_role}
    
    Identify skill gaps and provide a learning roadmap with specific resources."""
    
    response = model.generate_content(prompt)
    return response.text

# Resume tips generator
def generate_resume_tips(job_title, experience_level):
    prompt = f"""Generate specific resume tips for:
    Job Title: {job_title}
    Experience Level: {experience_level}
    
    Provide 5 actionable tips with examples."""
    
    response = model.generate_content(prompt)
    return response.text

# Job market insights
def get_market_insights(field, location):
    prompt = f"""Provide job market insights for:
    Field: {field}
    Location: {location}
    
    Include salary ranges, growth prospects, and in-demand skills."""
    
    response = model.generate_content(prompt)
    return response.text

# Learning resources recommender
def recommend_resources(skill, learning_style):
    prompt = f"""Recommend learning resources for:
    Skill: {skill}
    Learning Style: {learning_style}
    
    Suggest specific courses, books, and practice platforms."""
    
    response = model.generate_content(prompt)
    return response.text

# Create the interface
with gr.Blocks(theme=gr.themes.Soft(), title="AI Career & Skills Advisor") as demo:
    gr.Markdown("# 🎯 AI Career & Skills Advisor")
    gr.Markdown("*Powered by Gemini - Your personal career guidance assistant*")
    
    with gr.Tabs():
        # Main Chat Tab
        with gr.Tab("💬 Chat Assistant"):
            chatbot = gr.Chatbot(height=400)
            msg = gr.Textbox(placeholder="Ask about careers, skills, or resources...", label="Your Message")
            clear = gr.Button("Clear Chat")
            
            msg.submit(career_chatbot, [msg, chatbot], [msg, chatbot])
            clear.click(lambda: None, None, chatbot, queue=False)
        
        # Career Assessment Tab
        with gr.Tab("📋 Career Assessment"):
            gr.Markdown("### Quick Career Assessment")
            q1 = gr.Radio(["Remote", "Office", "Hybrid"], label=quiz_questions[0])
            q2 = gr.Radio(["With people", "Independent", "Mixed"], label=quiz_questions[1])
            q3 = gr.Radio(["Creative", "Analytical", "Both"], label=quiz_questions[2])
            q4 = gr.Radio(["High priority", "Moderate", "Work-focused"], label=quiz_questions[3])
            q5 = gr.Radio(["Stable routine", "Dynamic tasks", "Balanced"], label=quiz_questions[4])
            
            assess_btn = gr.Button("Get Career Recommendations")
            assessment_output = gr.Textbox(label="Career Recommendations", lines=8)
            
            assess_btn.click(assess_career, [q1, q2, q3, q4, q5], assessment_output)
        
        # Skill Gap Analysis Tab
        with gr.Tab("🎯 Skill Analysis"):
            gr.Markdown("### Skill Gap Analysis")
            current_skills = gr.Textbox(label="Current Skills (comma-separated)", placeholder="Python, SQL, Excel...")
            target_role = gr.Textbox(label="Target Role", placeholder="Data Scientist, Product Manager...")
            
            analyze_btn = gr.Button("Analyze Skills")
            skills_output = gr.Textbox(label="Skill Gap Analysis", lines=8)
            
            analyze_btn.click(analyze_skills, [current_skills, target_role], skills_output)
        
        # Resume Tips Tab
        with gr.Tab("📄 Resume Tips"):
            gr.Markdown("### Resume Optimization")
            job_title = gr.Textbox(label="Target Job Title", placeholder="Software Engineer, Marketing Manager...")
            experience = gr.Radio(["Entry Level", "Mid Level", "Senior Level"], label="Experience Level")
            
            resume_btn = gr.Button("Get Resume Tips")
            resume_output = gr.Textbox(label="Resume Tips", lines=8)
            
            resume_btn.click(generate_resume_tips, [job_title, experience], resume_output)
        
        # Market Insights Tab
        with gr.Tab("📊 Market Insights"):
            gr.Markdown("### Job Market Analysis")
            field = gr.Textbox(label="Field/Industry", placeholder="Technology, Healthcare, Finance...")
            location = gr.Textbox(label="Location", placeholder="San Francisco, Remote, India...")
            
            market_btn = gr.Button("Get Market Insights")
            market_output = gr.Textbox(label="Market Analysis", lines=8)
            
            market_btn.click(get_market_insights, [field, location], market_output)
        
        # Learning Resources Tab
        with gr.Tab("📚 Learning Resources"):
            gr.Markdown("### Personalized Learning Recommendations")
            skill = gr.Textbox(label="Skill to Learn", placeholder="Machine Learning, Public Speaking...")
            style = gr.Radio(["Visual", "Hands-on", "Reading", "Video"], label="Learning Style")
            
            learn_btn = gr.Button("Get Resources")
            learn_output = gr.Textbox(label="Learning Resources", lines=8)
            
            learn_btn.click(recommend_resources, [skill, style], learn_output)

demo.launch(share=True)
# 🎯 Enhanced Career & Skills Advisor Chatbot

## 📌 Overview
A comprehensive AI-powered career guidance platform that helps users explore career paths, assess skills, and receive personalized recommendations. Built with **Gradio** and **Google Gemini AI** for intelligent, context-aware conversations.

## 🚀 Enhanced Features

### 💬 **Smart Chat Assistant**
- Context-aware conversations with chat history
- Personalized career guidance powered by Gemini AI
- Real-time Q&A with memory of previous interactions

### 📋 **Career Assessment Quiz**
- 5-question personality and preference assessment
- AI-generated career recommendations based on responses
- Tailored suggestions for work environment and role types

### 🎯 **Skill Gap Analysis**
- Compare current skills with target role requirements
- Identify specific skill gaps and learning priorities
- Personalized learning roadmap generation

### 📄 **Resume Optimization**
- Role-specific resume tips and best practices
- Experience-level appropriate guidance
- Actionable recommendations with examples

### 📊 **Job Market Insights**
- Real-time market analysis for specific fields and locations
- Salary range estimates and growth prospects
- In-demand skills identification

### 📚 **Learning Resources Recommender**
- Personalized course and resource suggestions
- Learning style-based recommendations
- Platform-specific guidance (courses, books, practice sites)

## 🧠 AI-Powered Intelligence
- **Google Gemini Pro** integration for advanced natural language understanding
- Context-aware responses that remember conversation history
- Personalized recommendations based on user preferences and goals

## 🛠️ Tech Stack
- **Python** - Core programming language
- **Gradio** - Interactive web interface
- **Google Generative AI (Gemini)** - AI conversation engine
- **python-dotenv** - Environment variable management

## 📁 Installation & Setup

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up API Key:**
   - Get your Gemini API key from Google AI Studio
   - Add it to the `.env` file:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```

3. **Run the Application:**
   ```bash
   python app.py
   ```

## 🎮 How to Use

1. **Chat Assistant**: Ask any career-related questions for instant AI-powered guidance
2. **Career Assessment**: Complete the 5-question quiz for personalized career recommendations
3. **Skill Analysis**: Input your current skills and target role for gap analysis
4. **Resume Tips**: Get specific resume optimization advice for your target position
5. **Market Insights**: Research job market trends for specific fields and locations
6. **Learning Resources**: Discover personalized learning paths based on your style

## 🔧 Configuration
Customize the chatbot behavior by editing `config.py`:
- Adjust chat history length
- Modify popular career fields
- Update learning platform recommendations

## 🚀 Future Enhancements
- Integration with job board APIs
- Voice interaction capabilities
- Multi-language support
- Advanced analytics dashboard
- Mobile app development

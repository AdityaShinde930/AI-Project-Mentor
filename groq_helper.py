from groq import Groq #imports groq api lib
from dotenv import load_dotenv #to read .env
import os #to Access env variable
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY")) #using api key groq creates connection

def generate_project_ideas(domain, difficulty, duration): #passes
    prompt = f"""
    Generate exactly 3 software project ideas.
    Domain: {domain}
    Difficulty: {difficulty}
    Duration: {duration}

    Return ONLY in this format:
    1|Project Name|One line description
    2|Project Name|One line description
    3|Project Name|One line description
    """

    response = client.chat.completions.create( # sends request to groq model
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}] #prompt to ai
    )
    return response.choices[0].message.content #returns output/text generated ai

def generate_project_details(project_name, duration): # pass proj name
    prompt = f"""
    You are an expert software architect.

    Project Name: {project_name}
    Duration: {duration}

    Generate:
    1. Project Overview
    2. Problem Statement
    3. Core Features
    4. Tech Stack
    5. Skills Required
    6. Development Roadmap
    7. How To Start
    8. Common Challenges

    For the Development Roadmap:
    - Generate the roadmap according to the given duration.
    - Do NOT mention weeks or months.
    - Do NOT write things like "2 weeks", "4 weeks", etc.
    - Use only Phase 1, Phase 2, Phase 3, and Phase 4.
    - Keep the roadmap realistic and achievable within the specified duration.

    Use this exact format:
    🚀 PROJECT OVERVIEW
    🎯 PROBLEM STATEMENT
    ✨ CORE FEATURES
    🛠 TECH STACK
    📚 SKILLS REQUIRED
    📅 DEVELOPMENT ROADMAP
    🚀 HOW TO START

    ⚠ COMMON CHALLENGES
    Keep the response concise and professional.
    """

    response = client.chat.completions.create( # sends request to groq model
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]  #prompt to ai
    )
    return response.choices[0].message.content  #returns text generated ai
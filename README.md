# AI Project Mentor

## Overview

AI Project Mentor is a terminal-based AI application that helps users discover project ideas based on their domain, difficulty level, and available time.

The application generates multiple project recommendations and provides a complete project blueprint, including features, tech stack, required skills, development roadmap, implementation steps, and common challenges.

## Features

* Generate AI-powered project ideas
* Select from multiple project recommendations
* Get a detailed project blueprint
* View required skills and technologies
* Receive a step-by-step development roadmap
* Learn how to start building the project
* Understand common implementation challenges

## Technologies Used

* Python
* Groq API
* Llama 3.3 70B Model
* python-dotenv

## Project Structure

AI_Project_Mentor/

* main.py
* groq_helper.py
* .env
* requirements.txt
* README.md

## Installation

1. Clone the repository

```bash
git clone <repository_url>
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Create a .env file

```env
GROQ_API_KEY=your_api_key
```

4. Run the application

```bash
python main.py
```

## Example Workflow

1. Enter Domain
2. Enter Difficulty
3. Enter Duration
4. Generate Project Ideas
5. Select a Project
6. View Complete Project Blueprint

## Future Enhancements

* Project Feasibility Analysis
* Learning Resource Recommendations
* Resume Impact Score
* Advanced Project Filtering

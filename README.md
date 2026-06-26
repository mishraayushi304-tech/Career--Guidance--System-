# Career Guidance System
An AI-powered web application that provides personalized career recommendations based on a student's skills, interests, and educational background. This system leverages Google's Gemini AI to analyze user inputs and generate actionable career advice, skill gap analysis, and a structured 6-month learning roadmap.
##  Features
- **Personalized Recommendations:** Get the top 3 career paths tailored to your specific profile.
- **Skill Gap Analysis:** Identify the missing skills you need to achieve your career goals and what to prioritize.
- **6-Month Roadmap:** A step-by-step month-by-month learning plan to guide your preparation.
- **Interactive UI:** A clean, easy-to-use web interface built with Streamlit.
## Tech Stack
- **Frontend/UI:** [Streamlit](https://streamlit.io/)
- **AI/LLM:** [Google Gemini API](https://aistudio.google.com/) (`gemini-2.5-flash`)
- **Language:** Python 3.x
##  Getting Started
Follow these steps to run the project on your local machine.
### 1. Clone the Repository
```bash
git clone https://github.com/mishraayushi304-tech/Career--Guidance--System-.git
cd Career--Guidance--System-
```
### 2. Create a Virtual Environment (Recommended)
Creating a virtual environment ensures that dependencies don't conflict with other Python projects on your system.
```bash
# On Windows
python -m venv venv
venv\Scripts\activate
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```
### 3. Install Dependencies
Install all required Python packages listed in `requirements.txt`:
```bash
pip install -r requirements.txt
```
### 4. Set Up Environment Variables
This project requires a Google Gemini API key to function.
1. Create a file named `.env` in the root folder of the project.
2. Add your Gemini API key to the `.env` file like this:
   ```env
   GEMINI_API_KEY="your_api_key_here"
   ```
   *(Note: The `.env` file is intentionally ignored in Git to keep your API key secure.)*
### 5. Run the Application
Start the Streamlit server to run the app:
```bash
streamlit run app.py
```
The application will automatically open in your default web browser at `http://localhost:8501`.
##  License
This project is licensed under the MIT License. (See the `LICENSE` file for details.)

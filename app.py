import streamlit as st
from gemini_helper import get_career_guidance

# Page Configuration
st.set_page_config(
    page_title="AI Career Guidance System",
    page_icon="🎯",
    layout="wide"
)

# Sidebar
with st.sidebar:
    st.title("🎯 Career Guide")
    st.markdown("---")
    st.write(
        "Get personalized career recommendations using Gemini AI."
    )


# Page Title
st.title("AI Career Guidance System")

# Description
st.write("Enter your skills, interests, and education to get personalized career guidance.")

# Skills Input
skills = st.text_area(
    "Enter Your Skills",
    placeholder="Example: Python, SQL, Machine Learning"
)

# Interests Input
interests = st.text_area(
    "Enter Your Interests",
    placeholder="Example: AI, Data Science, Web Development"
)

# Education Dropdown
education = st.selectbox(
    "Select Your Education",
    [
        "B.Tech",
        "BCA",
        "MCA",
        "B.Sc",
        "M.Tech",
        "Other"
    ]
)

# Button
if st.button("Get Career Advice"):
    
    if not skills or not interests:
        st.warning("Please enter both skills and interests.")
    
    else:
        prompt = f""" 
        You are an expert career counselor.

        Student skills:
        {skills}

        Student Interests:
        {interests}

        Education:
        {education}

        Provide the response in the following format:

        ## Top 3 Career Recommendations

        For each career:
        - Career Name
        - Why it suits the student

        ## Skill Gap Analysis

        - Current Skills
        - Missing Skills
        - Skills to Learn First

       ## 6-Month Learning Roadmap

       Month 1:
       Month 2:
       Month 3:
       Month 4:
       Month 5:
       Month 6:

       Keep the response concise and student-friendly.
       """

        with st.spinner("Generating career guidance..."):
            response = get_career_guidance(prompt)

        st.success("Career guidance generated successfully!")

        st.markdown (response)


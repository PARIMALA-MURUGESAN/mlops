import streamlit as st
import pickle
import pandas as pd

from utils import extract_text

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

skills_db = {
    "Data Scientist":[
        "python","machine learning",
        "pandas","numpy","sql"
    ],

    "Software Engineer":[
        "java","spring","sql",
        "dsa","oops"
    ],

    "Frontend Developer":[
        "html","css",
        "javascript","react"
    ],

    "Backend Developer":[
        "java","spring",
        "mysql","api"
    ],

    "Cloud Engineer":[
        "aws","docker",
        "kubernetes","linux"
    ],

    "AI Engineer":[
        "python","llm",
        "generative ai",
        "machine learning"
    ]
}

st.title("Employee Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf","docx","txt"]
)

if uploaded_file:

    resume_text = extract_text(uploaded_file)

    x = vectorizer.transform([resume_text])

    predicted_role = model.predict(x)[0]

    required_skills = skills_db[predicted_role]

    found_skills = []

    for skill in required_skills:
        if skill.lower() in resume_text:
            found_skills.append(skill)

    missing_skills = list(
        set(required_skills) -
        set(found_skills)
    )

    match_score = (
        len(found_skills) /
        len(required_skills)
    ) * 100

    st.success(
        f"Predicted Role: {predicted_role}"
    )

    st.write(
        f"Skill Match Score: {match_score:.2f}%"
    )

    st.subheader("Skills Found")

    for skill in found_skills:
        st.write("✅", skill)

    st.subheader("Recommended Skills")

    if missing_skills:
        for skill in missing_skills:
            st.write("📌 Learn:", skill)
    else:
        st.success(
            "Candidate already has all required skills"
        )

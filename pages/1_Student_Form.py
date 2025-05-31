import streamlit as st
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

st.title("📝 Enter Student Info")

with st.form("student_form"):
    gender = st.selectbox("Gender", ["male", "female"])
    ethnicity = st.selectbox("Race/Ethnicity", ["group A", "group B", "group C", "group D", "group E"])
    parental_level = st.selectbox("Parental Level of Education", [
        "some high school", "high school", "some college", "associate's degree", "bachelor's degree", "master's degree"
    ])
    lunch = st.selectbox("Lunch Type", ["standard", "free/reduced"])
    test_prep = st.selectbox("Test Preparation Course", ["none", "completed"])
    reading_score = st.slider("Reading Score", 0, 100)
    writing_score = st.slider("Writing Score", 0, 100)

    submit = st.form_submit_button("Predict Math Score")

if submit:
    data = CustomData(
        gender=gender,
        race_ethnicity=ethnicity,
        parental_level_of_education=parental_level,
        lunch=lunch,
        test_preparation_course=test_prep,
        reading_score=reading_score,
        writing_score=writing_score
    )

    pred_df = data.get_data_as_data_frame()
    predict_pipeline = PredictPipeline()
    result = predict_pipeline.predict(pred_df)

    st.success(f"🎯 Predicted Math Score: **{result[0]:.2f}**")

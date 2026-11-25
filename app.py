
import streamlit as st
import pandas as pd
import joblib

# Load saved model
model = joblib.load(
    "student_model.joblib"
)

# Page configuration
st.set_page_config(
    page_title="Student Pass Prediction",
    page_icon="🎓",
    layout="centered"
)

# App title
st.title("🎓 Student Learning Outcome Prediction")
st.write(
    "Enter student learning information "
    "to predict the pass/fail outcome."
)

st.warning(
    "For demonstration only. "
    "Do not use predictions to judge real students."
)

# Input form
with st.form("student_form"):

    hours_studied = st.number_input(
        "Hours Studied",
        min_value=0.0,
        max_value=24.0,
        value=5.0,
        step=0.5
    )

    attendance = st.slider(
        "Attendance (%)",
        min_value=0,
        max_value=100,
        value=75
    )

    practice_tests = st.number_input(
        "Practice Tests Completed",
        min_value=0,
        max_value=100,
        value=3,
        step=1
    )

    sleep_hours = st.number_input(
        "Sleep Hours",
        min_value=0.0,
        max_value=24.0,
        value=7.0,
        step=0.5
    )

    study_method = st.selectbox(
        "Study Method",
        ["self", "group", "video"]
    )

    submit = st.form_submit_button(
        "Predict Student Outcome"
    )

# Prediction
if submit:

    input_data = pd.DataFrame({
        "hours_studied": [hours_studied],
        "attendance": [attendance],
        "practice_tests": [practice_tests],
        "sleep_hours": [sleep_hours],
        "study_method": [study_method]
    })

    prediction = model.predict(input_data)[0]

    st.subheader("Prediction Result")

    if prediction == 1:

        st.success("Predicted Outcome: PASS")

    else:

        st.error("Predicted Outcome: FAIL")

    # Probability
    probabilities = model.predict_proba(input_data)[0]

    st.write(
        f"Probability of Pass: "
        f"{probabilities[1] * 100:.2f}%"
    )

    st.write(
        f"Probability of Fail: "
        f"{probabilities[0] * 100:.2f}%"
    )

    st.caption(
        "This is a model estimate, not a guarantee "
        "of actual academic performance."
    )

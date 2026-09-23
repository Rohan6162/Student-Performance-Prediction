import streamlit as st
import joblib
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)

# Load models
linear_model = joblib.load("src/linear_regression_model.pkl")
tree_model = joblib.load("src/decision_tree_model.pkl")
rf_model = joblib.load("src/random_forest_model.pkl")

# Title
st.title("🎓 Student Performance Predictor")

st.write(
    "Enter student information and select a Machine Learning model "
    "to predict the final score."
)

st.divider()

# Model selection
st.subheader("🤖 Select Machine Learning Model")

model_name = st.selectbox(
    "Choose a model:",
    [
        "Linear Regression",
        "Decision Tree",
        "Random Forest"
    ]
)

st.divider()

# Student information
st.subheader("📊 Student Information")

study_hours = st.number_input(
    "Study Hours per Day",
    min_value=0.0,
    max_value=24.0,
    value=5.0,
    step=0.5
)

attendance = st.number_input(
    "Attendance (%)",
    min_value=0.0,
    max_value=100.0,
    value=75.0,
    step=1.0
)

previous_score = st.number_input(
    "Previous Score",
    min_value=0.0,
    max_value=100.0,
    value=70.0,
    step=1.0
)

assignment_score = st.number_input(
    "Assignment Score",
    min_value=0.0,
    max_value=100.0,
    value=70.0,
    step=1.0
)

sleep_hours = st.number_input(
    "Sleep Hours per Day",
    min_value=0.0,
    max_value=24.0,
    value=7.0,
    step=0.5
)

study_sessions = st.number_input(
    "Study Sessions",
    min_value=0,
    max_value=20,
    value=5,
    step=1
)

st.divider()

# Prediction button
if st.button("🔮 Predict Final Score", use_container_width=True):

    student = pd.DataFrame({
        "study_hours": [study_hours],
        "attendance": [attendance],
        "previous_score": [previous_score],
        "assignment_score": [assignment_score],
        "sleep_hours": [sleep_hours],
        "study_sessions": [study_sessions]
    })

    # Select model
    if model_name == "Linear Regression":
        selected_model = linear_model

    elif model_name == "Decision Tree":
        selected_model = tree_model

    else:
        selected_model = rf_model

    # Prediction
    prediction = selected_model.predict(student)[0]

    # Keep prediction between 0 and 100
    prediction = max(0, min(100, prediction))

    # Display result
    st.subheader("📈 Prediction Result")

    st.metric(
        label=f"{model_name} Prediction",
        value=f"{prediction:.2f}/100"
    )

    if prediction >= 75:
        st.success("The model predicts a relatively high final score.")

    elif prediction >= 50:
        st.info("The model predicts a moderate final score.")

    else:
        st.warning("The model predicts a lower final score.")

st.divider()

# Model performance
st.subheader("📋 Model Performance")

performance = pd.DataFrame({
    "Model": [
        "Linear Regression",
        "Decision Tree",
        "Random Forest"
    ],
    "MAE": [
        4.90,
        6.11,
        5.21
    ],
    "MSE": [
        36.39,
        63.10,
        42.70
    ],
    "R² Score": [
        0.663,
        0.415,
        0.604
    ]
})

st.dataframe(
    performance,
    use_container_width=True,
    hide_index=True
)

st.caption(
    "Metrics are based on the test dataset used during model evaluation."
)
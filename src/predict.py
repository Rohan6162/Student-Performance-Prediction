import joblib
import pandas as pd

# Load trained model
model = joblib.load("src/linear_regression_model.pkl")

# Student information
study_hours = float(input("Enter study hours per day: "))
attendance = float(input("Enter attendance percentage: "))
previous_score = float(input("Enter previous score: "))
assignment_score = float(input("Enter assignment score: "))
sleep_hours = float(input("Enter sleep hours per day: "))
study_sessions = float(input("Enter number of study sessions: "))

# Create input data
student = pd.DataFrame({
    "study_hours": [study_hours],
    "attendance": [attendance],
    "previous_score": [previous_score],
    "assignment_score": [assignment_score],
    "sleep_hours": [sleep_hours],
    "study_sessions": [study_sessions]
})

# Make prediction
prediction = model.predict(student)

print("\nPredicted Final Score:", round(prediction[0], 2))
import pandas as pd
import numpy as np

# Make results reproducible
np.random.seed(42)

# Number of students
n = 500

# Generate student data
study_hours = np.round(np.random.uniform(1, 10, n), 1)
attendance = np.random.randint(50, 101, n)
previous_score = np.random.randint(40, 91, n)
assignment_score = np.random.randint(40, 101, n)
sleep_hours = np.round(np.random.uniform(5, 9, n), 1)
study_sessions = np.random.randint(1, 11, n)

# Calculate final score with some random variation
final_score = (
    0.25 * study_hours * 10
    + 0.20 * attendance
    + 0.25 * previous_score
    + 0.20 * assignment_score
    + 0.05 * sleep_hours * 10
    + 0.05 * study_sessions * 10
    + np.random.normal(0, 5, n)
)

# Keep scores between 0 and 100
final_score = np.clip(final_score, 0, 100)
final_score = np.round(final_score, 2)

# Create DataFrame
data = pd.DataFrame({
    "study_hours": study_hours,
    "attendance": attendance,
    "previous_score": previous_score,
    "assignment_score": assignment_score,
    "sleep_hours": sleep_hours,
    "study_sessions": study_sessions,
    "final_score": final_score
})

# Save dataset
data.to_csv("data/student_data.csv", index=False)

print("Dataset created successfully!")
print(data.head())
print("\nDataset shape:", data.shape)
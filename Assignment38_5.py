# Based on the dataset values, analyze whether:
# Higher StudyHours increase the chance of passing.
# Higher Attendance improves FinalResult.
# Write your observations in 4–5 lines.

import pandas as pd

df = pd.read_csv('student_performance_ml.csv')

print("Average StudyHours:")
print(df.groupby("FinalResult")["StudyHours"].mean())

print("\nAverage Attendance:")
print(df.groupby("FinalResult")["Attendance"].mean())
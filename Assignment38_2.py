# display the total number of students in the dataset.
# Count how many students Passed (FinalResult = 1).
# Count how many students Failed (FinalResult = 0).

import pandas as pd

df = pd.read_csv('student_performance_ml.csv')

total_students = len(df)

passed_student = (df["FinalResult"] == 1).sum()

failed_student = (df["FinalResult"] == 0).sum()

print("Total Students :", total_students)

print("Passed Students :", passed_student)

print("Failed student :", failed_student)
# Using pandas functions, calculate and display:
# Average StudyHours
# Average Attendance
# Maximum PreviousScore
# Minimum SleepHours

import pandas as pd

df = pd.read_csv('student_performance_ml.csv')

avg_studyhours = df["StudyHours"].mean()
avg_attendance = df["Attendance"].mean()
max_prevscore = df["PreviousScore"].max()
min_sleephours = df["SleepHours"].min()

print("Average studyhours :", avg_studyhours)
print("Average attendance :", avg_attendance)
print("Maximum previousScore :", max_prevscore )
print("Minimum sleephours :",min_sleephours )
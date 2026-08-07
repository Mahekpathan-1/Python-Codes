#Use value_counts() to analyze the distribution of FinalResult.
# Calculate the percentage of Pass and Fail students.
# Is the dataset balanced? Justify your answer.

import pandas as pd

df = pd.read_csv('student_performance_ml.csv')

result = df["FinalResult"].value_counts()

print("Pass/Fail count:")
print(result)

percentage = (result / len(df)) *100 

print("Pass/Fail percentage :")
print(percentage)

if abs(percentage[1] - percentage[0]) <= 10:
    print("Dataset is balanced")
else:
    print("Dataset is not balanced ")
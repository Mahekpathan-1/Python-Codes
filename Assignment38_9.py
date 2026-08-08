# Create a plot showing relationship between AssignmentsCompleted and FinalResult.
# Explain your observation.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("student_performance_ml.csv")

df["AssignmentsCompleted"] = pd.to_numeric(df["AssignmentsCompleted"],errors="coerce")

df = df.dropna(subset=["AssignmentsCompleted", "FinalResult"])

print(df[["AssignmentsCompleted", "FinalResult"]])

sns.scatterplot(
    x="AssignmentsCompleted",
    y="FinalResult",
    data=df,
    s=100
)

plt.title("Assignments Completed vs Final Result")
plt.xlabel("Assignments Completed")
plt.ylabel("Final Result")

plt.yticks(
    [0, 1],
    ["Fail", "Pass"]
)

plt.show()
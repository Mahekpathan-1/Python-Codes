# Plot SleepHours against FinalResult. Does sleeping more guarantee success? Explain.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("student_performance_ml.csv")

df["SleepHours"] = pd.to_numeric(df["SleepHours"],errors="coerce")

df = df.dropna(subset=["SleepHours", "FinalResult"])

print(df[["SleepHours", "FinalResult"]])

sns.scatterplot(
    x="SleepHours",
    y="FinalResult",
    data=df,
    s=100)

plt.title("Sleep Hours vs Final Result")
plt.xlabel("Sleep Hours")
plt.ylabel("Final Result")


plt.yticks(
    [0, 1],
    ["Fail", "Pass"]
)

plt.show()
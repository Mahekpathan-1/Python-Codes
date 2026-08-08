# boxplot for Attendance and identify outliers

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("student_performance_ml.csv")

sns.boxplot(y=df["Attendance"])

plt.title("Boxplot of Attendance")
plt.ylabel("Attendance")
plt.show()

Q1 = df["Attendance"].quantile(0.25)
Q3 = df["Attendance"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = df[
    (df["Attendance"] < lower_limit) |
    (df["Attendance"] > upper_limit)]

print("Outliers in Attendance:")
print(outliers["Attendance"])
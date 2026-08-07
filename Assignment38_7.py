# Load student_performance_ml.csv and display the required information

import pandas as pd

# Load CSV file
df = pd.read_csv("student_performance_ml.csv")

# First 5 records
print("First 5 Records:")
print(df.head())

# Last 5 records
print("\nLast 5 Records:")
print(df.tail())

# Total number of rows and columns
print("\nRows and Columns:")
print(df.shape)

# List of column names
print("\nColumn Names:")
print(df.columns.tolist())

# Data types of each column
print("\nData Types:")
print(df.dtypes)
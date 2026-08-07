import pandas as pd

df = pd.read_csv('student_performance_ml.csv')

print("\nFirst 5 Records : ")
print(df.head())

print("\nLast 5 Records : ")
print(df.tail())

print("\nTotal number of rows and columns :")
print(df.shape )

print("\nColumn names :")
print(df.columns.tolist())

print("Data types : ")
print(df.dtypes)
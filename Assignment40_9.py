# Create a new column:
# PerformanceIndex = (StudyHours * 2) + Attendance
# Train the Decision Tree using this new feature.
# Calculate testing accuracy.
# Compare it with the previous full-feature accuracy.
# Check whether accuracy improves.

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree

def main():
    
    df = pd.read_csv('student_performance_ml.csv')
    
    df["PerformanceIndex"] = (df["StudyHours"] * 2) + df["Attendance"]

    print("New PerformanceIndex column:")
    print(df[["StudyHours", "Attendance", "PerformanceIndex"]])
    
    X= df.drop("FinalResult", axis=1)
    
    Y= df["FinalResult"]
    
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y, train_size=0.5, random_state=42)
    
    model = DecisionTreeClassifier()
    
    model = model.fit(X_train,Y_train)
    
    Y_pred = model.predict(X_test)

    new_accuracy = accuracy_score(Y_test, Y_pred)

    print("\nNew Testing Accuracy :",new_accuracy * 100, "%")
    
    previous_accuracy = 100.0

    print("Previous Testing Accuracy :",previous_accuracy, "%")

    if new_accuracy * 100 > previous_accuracy:

        print("Accuracy improved after adding PerformanceIndex.")

    elif new_accuracy * 100 < previous_accuracy:

        print("Accuracy decreased after adding PerformanceIndex.")

    else:

        print("Accuracy remained the same after adding PerformanceIndex.")


    
if __name__ =="__main__":
    main()
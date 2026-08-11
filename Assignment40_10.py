# Train a Decision Tree with max_depth = None.
# Calculate training accuracy.
# Calculate testing accuracy.
# Explain why training accuracy can be 100% while testing accuracy is lower.

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def main():
    df = pd.read_csv("student_performance_ml.csv")

    X = df.drop("FinalResult", axis=1)
    Y = df["FinalResult"]

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)
    
    model = DecisionTreeClassifier(max_depth=None,random_state=42)

    model.fit(X_train, Y_train)

    print("Decision Tree trained successfully")
    
    Y_train_pred = model.predict(X_train)

    train_accuracy = accuracy_score(Y_train,Y_train_pred)

    print("\nTraining Accuracy :",train_accuracy * 100, "%")
    
    Y_test_pred = model.predict(X_test)

    test_accuracy = accuracy_score( Y_test,Y_test_pred)

    print("Testing Accuracy  :",test_accuracy * 100, "%")


if __name__ == "__main__":
    main()
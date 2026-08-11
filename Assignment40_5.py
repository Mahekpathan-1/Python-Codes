# Do not use accuracy_score.
# Manually count correct predictions.
# Calculate accuracy using the formula.
# Compare it with sklearn's accuracy.

import pandas as pd

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

def main():
    
    df = pd.read_csv('student_performance_ml.csv')
    
    X= df.drop("FinalResult", axis=1)
    
    Y= df["FinalResult"]
    
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y, train_size=0.5, random_state=42)
    
    model = DecisionTreeClassifier()
    
    model = model.fit(X_train,Y_train)
    
    Y_pred = model.predict(X_test)
    
    correct = 0

    for actual, predicted in zip(Y_test, Y_pred):

        if actual == predicted:
            correct = correct + 1

    total = len(Y_test)

    manual_accuracy = (correct / total) * 100

    print("Correct Predictions :", correct)
    print("Total Predictions :", total)

    print("Manual Accuracy :", manual_accuracy, "%")
    
    sklearn_accuracy = accuracy_score(Y_test,Y_pred)
    
    print("Accuracy using sklearn is :", sklearn_accuracy * 100 , "%")
    
if __name__ =="__main__":
    main()

    
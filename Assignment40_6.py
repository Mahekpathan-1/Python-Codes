# Compare actual values (Y_test) with predicted values (Y_pred).
# Find the students where the prediction is incorrect.
# Display those students.
# Count the number of misclassified students.
# Observe any common pattern.

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
    
    misclassified  = Y_test != Y_pred
    
    print("Misclassified Student :")
    print("-"* 40)
    
    print(X_test[misclassified])
    
    print("Actual results:")
    print(Y_test[misclassified])
    
    print("Predicted  results:")
    print(Y_pred[misclassified])
    
    count = misclassified.sum()
    
    print("Number of misclassified student :", count)
    
if __name__ == "__main__":
    main()
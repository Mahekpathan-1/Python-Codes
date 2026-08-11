# Train a Decision Tree using only StudyHours and Attendance.
# Calculate testing accuracy.
# Compare it with the full-feature model.
# Decide whether the model is still performing well.

import pandas as pd

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

def main():
    
    df = pd.read_csv('student_performance_ml.csv')
    
    X= df[["StudyHours","Attendance"]]
    
    Y= df["FinalResult"]
    
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y, train_size=0.5, random_state=42)
    
    model = DecisionTreeClassifier()
    
    model = model.fit(X_train,Y_train)
    
    print("Decision tree trained succesfully")
    
    Y_pred = model.predict(X_test)
    
    new_accuracy = accuracy_score(Y_test,Y_pred)
    print("Accuracy using studyhours and Attendance is :", new_accuracy * 100 ,"%")
    
    full_feature_accuracy = 100.0
    
    print("Full feature model accuracy is :", full_feature_accuracy *100, "%")
    
    if new_accuracy * 100 > full_feature_accuracy :
        print("The model is still performing well")
        
    else:
        print("Accuracy is decresed when only two features used")

    
if __name__ == "__main__":
    main()
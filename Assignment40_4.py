# Create a new DataFrame containing 5 students.
# Give their StudyHours and Attendance.
# Use the trained model to predict their FinalResult.
# Display the predictions clearly.

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
    
    new_students = pd.DataFrame({
        "StudyHours": [6, 8, 4, 7, 5],
        "Attendance": [85, 90, 65, 88, 75]
    })
    
    prediction = model.predict(new_students)
    
    print("Prediction for 5 new students :")
    
    new_students["predictedresult"] = prediction
    print(new_students)

if __name__ == "__main__":
    main()
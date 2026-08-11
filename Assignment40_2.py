# Remove the SleepHours column from the dataset.
# Train the Decision Tree model again.
# Calculate the new testing accuracy.
# Compare the new accuracy with the previous accuracy.
# Determine whether removing SleepHours affects model performance.

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def main():
    
    df = pd.read_csv('student_performance_ml.csv')
        
    X = df.drop(["FinalResult","SleepHours"], axis = 1)
    Y = df["FinalResult"]
        
    X_train , X_test , Y_train , Y_test = train_test_split(X, Y , test_size= 0.2 , random_state= 42)
        
    model = DecisionTreeClassifier()
        
    model = model.fit(X_train, Y_train)
        
    print("Decision tree trained successfully")
    
    Y_pred = model.predict(X_test)
    
    print("Expected Answer:")
    print(Y_test)
    
    print("Predicted Answer :")
    print(Y_pred)
        
    new_accuracy = accuracy_score(Y_test, Y_pred)
    
    print("New Accuracy is :", new_accuracy * 100)
    
    previous_accuracy = 100.0
    
    print("Previous Testing Accuracy :", previous_accuracy, "%")
    
    if new_accuracy * 100 > previous_accuracy:
       print("Accuracy increased after removing SleepHours.")
       
    elif new_accuracy * 100 < previous_accuracy:
        print("Accuracy decreased after removing SleepHours.")

    else:
       print("Accuracy remained the same after removing SleepHours.")
       
if __name__ == "__main__":
    main()

# Use the trained model to predict the test data and show Predicted vs Actual values.

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

def main():
    
    df = pd.read_csv('student_performance_ml.csv')
    
    X = df.drop("FinalResult", axis = 1)
    Y = df["FinalResult"]
    
    X_train, X_test, Y_train , Y_test = train_test_split(X, Y, test_size= 0.2, random_state=42)
    
    model = DecisionTreeClassifier()
    
    model = model.fit(X_train,Y_train)
    
    Y_pred = model.predict(X_test)
    
    print("predicted\t Actual")
    print("-------------------")
    
    for predicted, actual in zip (Y_pred, Y_test):
        print(predicted ,"\t\t", actual)
    
if __name__ == "__main__":
    main()
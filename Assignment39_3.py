# Accuracy of the Decision Tree classification

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

def main():
    
    df = pd.read_csv('student_performance_ml.csv')
    
    X = df.drop("FinalResult", axis = 1)
    Y = df["FinalResult"]
    
    X_train, X_test, Y_train , Y_test = train_test_split(X, Y, test_size= 0.2, random_state=42)
    
    model = DecisionTreeClassifier()
    
    model = model.fit(X_train,Y_train)
    
    Y_pred = model.predict(X_test)
    
    accuracy = accuracy_score(Y_test, Y_pred)
    
    print("Decision Tree Accuracy is :", accuracy * 100 , "%")
    
if __name__ == "__main__":
    main()
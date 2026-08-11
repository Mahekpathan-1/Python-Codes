# Create and train the Decision Tree mode

from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from sklearn.model_selection import train_test_split

def main():
    
    df = pd.read_csv('student_performance_ml.csv')
    
    X = df.drop("FinalResult", axis = 1)
    Y = df["FinalResult"]
    
    X_train , X_test , Y_train , Y_test = train_test_split(X, Y , test_size= 0.2 , random_state= 42)
    
    model = DecisionTreeClassifier()
    
    model = model.fit(X_train, Y_train)
    
    print("Decision tree trained successfully")
    
if __name__ =="__main__":
    main()
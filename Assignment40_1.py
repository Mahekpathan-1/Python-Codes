#After training the Decision Tree model, use:
# model.feature_importances_
# to:
# Display the importance score of every feature.
# Find which feature contributes the most to predicting the result.
# Find which feature contributes the least.

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
    
    importance = model.feature_importances_
    
    print("Feature Importance")
    print("-"*40)
    
    for feature , score in zip (X.columns, importance):
        print(feature, ":", score)
        
    most_importance = X.columns[importance.argmax()]
    
    least_importance = X.columns[importance. argmin()]
    
    print("Most important features :", most_importance)
    
    print("Least important features :", least_importance)
    
if __name__ =="__main__":
    main()
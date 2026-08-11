# Train the Decision Tree with random_state = 0.
# Train it again with random_state = 10.
# Train it again with random_state = 42.
# Calculate testing accuracy for each model.
# Compare the accuracies and check whether the result changes.

import pandas as pd

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

def main():
    
    df = pd.read_csv('student_performance_ml.csv')
    
    X= df.drop("FinalResult", axis=1)
    
    Y= df["FinalResult"]
    
    ######################################
    # model 1 : random state = 0
    ######################################
    
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y, train_size=0.5, random_state=0)
    
    model1 = DecisionTreeClassifier()
    
    model1 = model1.fit(X_train,Y_train)
    
    Y_pred1 = model1.predict(X_test)
    
    accuracy1 = accuracy_score(Y_test,Y_pred1)
    
    print("random state = 0 ")
    print("Testing Accuracy is :" , accuracy1 * 100 ,"%")
    
    
    ######################################
    # model 2 : random state = 10
    ######################################
        
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y, train_size=0.5, random_state=10)
        
    model2 = DecisionTreeClassifier()
        
    model2 = model2.fit(X_train,Y_train)
        
    Y_pred2 = model2.predict(X_test)
        
    accuracy2 = accuracy_score(Y_test,Y_pred2)
        
    print("random state = 10 ")
    print("Testing Accuracy is :" , accuracy2 * 100 ,"%")
    
    ######################################
    # model 3 : random state = 42
    ######################################
            
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y, train_size=0.5, random_state=42)
            
    model3 = DecisionTreeClassifier()
            
    model3 = model3.fit(X_train,Y_train)
            
    Y_pred3 = model3.predict(X_test)
            
    accuracy3 = accuracy_score(Y_test,Y_pred3)
            
    print("random state = 42 ")
    print("Testing Accuracy is :" , accuracy3 * 100 ,"%")
        
if __name__ =="__main__":
    main()
        
    
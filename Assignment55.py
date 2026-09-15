import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.ensemble import VotingClassifier


def main():
    
    #---------------------------------------------
    # Step 1. Load the dataset
    #---------------------------------------------
    Border = "-"*40
    
    print(Border)
    print("Step 1. Load the dataset")
    print(Border)
    
    df = pd.read_csv("Customer_Loan_Approval.csv")
    
    print(df.head())
    
    #---------------------------------------------
    # Step 2. Check Missing values 
    #---------------------------------------------
    
    print(Border)
    print("Step 2. Check Missing values ")
    print(Border)
    
    print("Missing Values\n", df.isnull().sum())
    
    #---------------------------------------------
    # Step 3.Separate input and output variables
    #---------------------------------------------
    
    print(Border)
    print("Step 3.Separate input and output variables")
    print(Border)
    
    X = df.drop(['LoanApproved'], axis=1)
    Y = df['LoanApproved']
    
    print("Shape of X :", X.shape)
    print("Shape of Y :", Y.shape)
    
    #---------------------------------------------
    # Step 4. Split dataset into training and testing
    #---------------------------------------------
    
    print(Border)
    print("Step 4. Split dataset into training and testing")
    print(Border)
    
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.30, random_state=42)
    
    scaler = StandardScaler()
    
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.fit_transform(X_test)
    
    print("Spliting of dataset sucsfully completed ")
    print(Border)
    
    #---------------------------------------------
    # Step 5.Train Logistic Regression 
    #---------------------------------------------
    
    print(Border)
    print("Step 5.Train Logistic Regression and calculate accuracy")
    print(Border)
    
    model_log = LogisticRegression()
    
    model_log.fit(X_train_scaled, Y_train)
    
    Y_pred_log = model_log.predict(X_test_scaled)
    
    accuracy = accuracy_score(Y_test, Y_pred_log)
    
    print("Logistic Regression accuracy\n", accuracy)
    print(Border)
    
    #---------------------------------------------
    # Step 6. Train DecisionTree
    #--------------------------------------------
    
    print(Border)
    print("Step 6. Train DecisionTree and calculate accuracy")
    print(Border)
    
    model_Decision = DecisionTreeClassifier()
    
    model_Decision.fit(X_train_scaled, Y_train)
        
    Y_pred_log = model_Decision.predict(X_test_scaled)
        
    accuracy = accuracy_score(Y_test, Y_pred_log)
    
    print("DecisionTree accuracy :\n", accuracy)
    print(Border)
    
    #---------------------------------------------
    # Step 7. Train KNN
    #--------------------------------------------
    
    print(Border)
    print("Step 7. Train KNN and calculate accuracy")
    print(Border)
    
    Model_KNN = KNeighborsClassifier()
    Model_KNN.fit(X_train_scaled, Y_train)
    
    Y_pred_log = Model_KNN.predict(X_test_scaled)
    
    accuracy = accuracy_score(Y_test, Y_pred_log)
    
    print("KNN accuracy :\n", accuracy)
    print(Border)
    
    #---------------------------------------------
    # Step 8. Hard Voting Classifier
    #--------------------------------------------
    
    print(Border)
    print("Step 8. Hard Voting Classifier")
    print(Border)
    
    model = VotingClassifier(
        estimators= [
            ('logistic', model_log),
            ('decision_tree', model_Decision),
            ('Knn', Model_KNN)
            ],
        voting="hard"
    )
    
    model = model.fit(X_train_scaled, Y_train)
    
    #---------------------------------------------
    # Step 9. Calculate accuracy
    #--------------------------------------------
    
    print(Border)
    print("Step 9. calculate hard voting accuracy")
    print(Border)
        
    Y_pred_voting = model.predict(X_test_scaled)
    
    Hard_accuracy = accuracy_score(Y_test, Y_pred_voting)
    
    print("Hard voting classifier accuracy :", Hard_accuracy)
    
    #---------------------------------------------
    # Step 10. Soft Voting Classifier
    #--------------------------------------------
    
    print(Border)
    print("Step 8. soft Voting Classifier")
    print(Border)

    model = VotingClassifier(
    estimators= [
        ('logistic', model_log),
        ("decision_tree",model_Decision),
        ('Knn', Model_KNN)
    ],
    voting='soft'
)
    
    model = model.fit(X_train_scaled, Y_train)
    
    #---------------------------------------------
    # Step 11. Calculate accuracy
    #--------------------------------------------
    
    print(Border)
    print("Step 9. calculate  soft voting accuracy")
    print(Border)
    
    Y_pred_vote = model.predict(X_test_scaled)
    
    Soft_accuracy = accuracy_score(Y_test, Y_pred_vote)
    
    print("Soft Voting classifier acuracy is :", Soft_accuracy)  
    
    #---------------------------------------------
    # Step 12. Compare
    #--------------------------------------------
    
    print(Border)
    print("Step 12. Compare Hard Voting and Soft Voting")
    print(Border)

    print("Hard Voting Accuracy :", Hard_accuracy)
    print("Soft Voting Accuracy :", Soft_accuracy)

    if Hard_accuracy > Soft_accuracy:
       print("Hard Voting gives better accuracy.")

    elif Soft_accuracy > Hard_accuracy:
        print("Soft Voting gives better accuracy.")

    else:
        print("Both Hard Voting and Soft Voting give the same accuracy.")  
            
            
if __name__ == "__main__":
    main()
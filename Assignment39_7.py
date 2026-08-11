# Use train model predict the result

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt
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
    
    cm = confusion_matrix(Y_test, Y_pred)
    
    print("Confusion matrix :")
    print(cm)
    
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    
    train_pred = model.predict(X_train)

    train_accuracy = accuracy_score(Y_train, train_pred)

    print("Training Accuracy :", train_accuracy * 100, "%")
    
    disp.plot()
    
    plt.title("Decision tree confusion matrics")
    plt.show()
    
    # Max_dept = 1
    
    model1 = DecisionTreeClassifier(max_depth=1, random_state=42)
    
    model1 = model1.fit(X_train, Y_train)
    
    Y_pred1 = model1.predict(X_test)
    
    accuracy1 = accuracy_score ( Y_test,Y_pred1)
    
    # Max_dept = 3
    
    model2 = DecisionTreeClassifier(max_depth=3, random_state=42)
    
    model2 = model2.fit(X_train, Y_train)
    
    Y_pred2 = model2.predict(X_test)
    
    accuracy2 = accuracy_score(Y_test, Y_pred2)
    
    # max_dept = none
    
    model3 = DecisionTreeClassifier(max_depth=None, random_state=42)
        
    model3 = model3.fit(X_train, Y_train)
        
    Y_pred3 = model3.predict(X_test)
        
    accuracy3 = accuracy_score(Y_test, Y_pred3)
    
    print("Max depth : 1", accuracy1 * 100, "%")
        
    print("Max depth : 3", accuracy3 * 100, "%")
    
    print("Max depth : None", accuracy1 * 100, "%")
    
    print("-"*40)
    
    print("The testing accuracy of all three Decision Tree models is 100%. Therefore, all three models perform equally well on the given testing dataset. Changing max_depth from 1 to 3 or None does not change the testing accuracy.")
    
    print("-"*40)
    
    student = pd.DataFrame({
    "StudyHours": [6],
    "Attendance": [85],
    "PreviousScore": [66],
    "AssignmentsCompleted": [7],
    "SleepHours": [7]
})

    
    prediction = model.predict(student)
    
    print("Prediction :", prediction)
    
    if prediction[0] == 1:
        print("The student will pass ")
        
    else:
        print("The student will fail")
    
if __name__ == "__main__":
    main()
# training accuracy
# testing accuracy
# Compare both and comment whether the model is overfitting or underfitting.

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
    
if __name__ == "__main__":
    main()
# Train a Decision Tree model.
# Visualize the trained tree using plot_tree().
# Find which feature appears at the root node.
# Explain why that feature was selected first.

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree

def main():
    
    df = pd.read_csv('student_performance_ml.csv')
    
    X= df.drop("FinalResult", axis=1)
    
    Y= df["FinalResult"]
    
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y, train_size=0.5, random_state=42)
    
    model = DecisionTreeClassifier()
    
    model = model.fit(X_train,Y_train)
    
    Y_pred = model.predict(X_test)
    
    plot_tree(
    model,
    feature_names=X.columns,
    class_names=["Fail", "Pass"],
    filled=True
)
    
    plt.title("Decision Tree Visualization")
    plt.show()

    root_index = model.tree_.feature[0]

    root_feature = X.columns[root_index]

    print("\nRoot Node Feature :", root_feature)
    
if __name__ == "__main__":
    main()
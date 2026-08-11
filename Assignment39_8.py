import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import (confusion_matrix,accuracy_score,classification_report,ConfusionMatrixDisplay)

Border = "-"* 40

#############################################################
# Step 1 : Load the Dataset
#############################################################

print(Border)
print("Step 1 : Load the Dataset")
print(Border)

Datapath = 'student_performance_ml.csv'

df = pd.read_csv(Datapath)

print("Dataset loaded successfully")
print("Initial entries are :")
print(df.head())

print(Border)

#############################################################
# Step 2 : Data Analysis (EDA)
#############################################################

print(Border)
print("Step 2 : Data Analysis (EDA)")
print(Border)

print("Shape of dataset :", df.shape)
print(Border)

print("colums names :", list(df.columns))
print(Border)

print("Missing value per column :")
print(df.isnull().sum())
print(Border)

print("result check (result count)")
print(df["FinalResult"].value_counts())
print(Border)

print("Statistical report of dataset")
print(df.describe())

#############################################################
# Step 3 : Visualization of dataset
#############################################################

print(Border)
print("Step 3 : Visualization of dataset")
print(Border)

df['FinalResult'].value_counts().plot(kind = "bar")

plt.title("Student Result Distribution")

plt.xlabel("FinalResult")
plt.ylabel("Number of Students")

plt.legend()
plt.grid()
plt.show()

#############################################################
# Step 4 : Split the dataset for training and testing
#############################################################

print(Border)
print("Step 4 : Split the dataset for training and testing")
print(Border)

X = df.drop("FinalResult", axis=1)
Y = df["FinalResult"]

X_train, X_test, Y_train, Y_test = train_test_split( X, Y, test_size=0.5,random_state=42)

print("Dataset splitting activity done")

print("X :",X.shape)   #(150,4)
print("Y :",Y.shape)   #(150,)

print("X_train :",X_train.shape)  #(75,4)
print("X_test :",X_test.shape)    #(75,4)

print("Y_train :",Y_train.shape)  #(75)
print("Y_test :",Y_test.shape)    #(75)

#############################################################
# Step 5 : Train the model
#############################################################

print(Border)
print("Step 5 : Train the model")
print(Border)

model = DecisionTreeClassifier(max_depth=5)

model.fit(X_train,Y_train)

print("Model train succesfully")

#############################################################
# Step 6 : Prediction of model
#############################################################

print(Border)
print("Step 6 : Prediction of model")
print(Border)

Y_pred = model.predict(X_test)

print("Testing done succesfully")

print("Expected answer :")
print(Y_test)

print("Predicted Answer :")
print(Y_pred)

#############################################################
# Step 7 : Accuracy Calculation
#############################################################

print(Border)
print("Step 7 : Accuracy Calculation")
print(Border)

accuracy = accuracy_score(Y_test,Y_pred)
print("Accuracy of model is :", accuracy* 100)

train_accuracy = accuracy_score(Y_train, Y_pred)

print("Training accuracy is :", train_accuracy)

test_accuracy = accuracy_score(Y_test, Y_pred)

print("Testing accuracy is :", test_accuracy)

#############################################################
# Step 8 : confusion matrix generation
#############################################################

print(Border)
print("Step 8 : confusion matrix generation")
print(Border)

print("Confusion matrix ")
cm = confusion_matrix(Y_test,Y_pred)
print(cm)

#############################################################
# Step 8 : confusion matrix generation
#############################################################

print(Border)
print("Step 8 : confusion matrix generation")
print(Border)

disp = ConfusionMatrixDisplay(confusion_matrix=cm)

disp.plot()

plt.title("Decision tree Confusion matrix ")
plt.show()

#############################################################
# Step 9 : Final Conclusion
#############################################################

print(Border)
print("Step 9 : Final Conclusion")
print(Border)

# Final Conclusion

# Final Conclusion

print("\nFinal Conclusion:")

if train_accuracy == test_accuracy:

    print("Training Accuracy :", train_accuracy * 100, "%")
    print("Testing Accuracy  :", test_accuracy * 100, "%")

    if train_accuracy == 1.0:
        print("The model performs very well on both training and testing data.")
        print("There is no difference between training and testing accuracy.")
        print("The model does not show clear signs of overfitting or underfitting.")

    else:
        print("Training and testing accuracies are equal.")
        print("The model has similar performance on both datasets.")

elif train_accuracy > test_accuracy:

    print("Training Accuracy :", train_accuracy * 100, "%")
    print("Testing Accuracy  :", test_accuracy * 100, "%")

    print("Training accuracy is higher than testing accuracy.")

    if train_accuracy - test_accuracy > 0.10:
        print("The model may be overfitting.")
    else:
        print("The difference is small, so the model is performing reasonably well.")

else:

    print("Training Accuracy :", train_accuracy * 100, "%")
    print("Testing Accuracy  :", test_accuracy * 100, "%")

    print("Testing accuracy is higher than training accuracy.")
    print("The model does not show signs of overfitting.")
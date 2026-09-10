import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, ConfusionMatrixDisplay


#--------------------------------------------------------
# Step 1. Load Dataset
#--------------------------------------------------------

Border= "-"* 50
print(Border)
print("Step 1. Load Dataset")
print(Border)

df = pd.read_csv("Employee_Attrition.csv")

print("Dataset Load Succesfully")
print(Border)

#--------------------------------------------------------
# Step 2. Display Shape, columns and first five records
#--------------------------------------------------------

print(Border)
print("Step 2. Display Shape, columns and first five records")
print(Border)

print("Shape of Dataset :", df.shape)
print(Border)
print("Columns :", df.columns)
print(Border)
print("First Five Records:")
print(df.head())
print(Border)

#--------------------------------------------------------
# Step 3. Check Missing Values 
#--------------------------------------------------------
print(Border)
print("Step 3. Check Missing Values")
print(Border)

print("Missing Values :\n", df.isnull().sum())
print(Border)

#--------------------------------------------------------
# Step 4. Identify Numerical And Categorical Features 
#--------------------------------------------------------

print(Border)
print("Step 4. Identify Numerical And Categorical Features ")
print(Border)

print("Numerical Features:")
print(df.select_dtypes(include=['number']).columns.tolist())

print(Border)
print("Categorical Features:")
print(df.select_dtypes(include=['str','category']).columns.tolist())
print(Border)

#--------------------------------------------------------
# Step 5. convert categorical features such as Overtime into numerical representation
#--------------------------------------------------------

print(Border)
print(" Step 5. convert categorical features such as Overtime into numerical representation")
print(Border)

LE = LabelEncoder()

df['OverTime']= LE.fit_transform(df["OverTime"])

print(df.head())
print(Border)

#--------------------------------------------------------
# Step 6.Convert the target Attrition in to 0 and 1
#--------------------------------------------------------

print(Border)
print("Step 6.Convert the target Attrition in to 0 and 1")
print(Border)

df['Attrition'] = LE.fit_transform(df["Attrition"])

print(df.head())
print(Border)

#--------------------------------------------------------
# Step 7. Separate Independent and Dependent Variables
#-------------------------------------------------------

print(Border)
print("Step 7. Separate Independent and Dependent Variables")
print(Border)

X = df.drop(['Attrition'], axis=1)

Y = df['Attrition']

print("Shape of X :", X.shape)
print("Shape of Y :", Y.shape)

print(Border)

#--------------------------------------------------------
# Step 8. Split dataset into training and testing data 
#-------------------------------------------------------

print(Border)
print("Step 8. Split dataset into training and testing data ")
print(Border)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.30, random_state=42)

print("Dataset Divide sucesfully")
print(Border)

#--------------------------------------------------------
# Step 9. Feature Scalling
#-------------------------------------------------------

print(Border)
print("Step 9. Feature Scalling")
print(Border)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)

print("Scaled Training data")
print(X_train_scaled[:5])

print(Border)

#--------------------------------------------------------
# Step 10. MLP with two hidden layers 
#--------------------------------------------------------

print(Border)
print("Step 10. MLP with two hidden layers ")
print(Border)

model = MLPClassifier(
    hidden_layer_sizes=(8,4),
    activation='relu',
    solver='adam',
    max_iter=1000,
    random_state=42
)

print(model)
print(Border)

#--------------------------------------------------------
# Step 11. Train the Network
#--------------------------------------------------------

print(Border)
print("Step 11. Train the Network")
print(Border)

model.fit(X_train_scaled,Y_train)

print("Model training completed")
print(Border)

#--------------------------------------------------------
# Step 12. Number of iteration required fro training
#--------------------------------------------------------

print(Border)
print("Step 12. Number of iteration required for training")
print(Border)

print("Number of iteration required for training:\n", model.n_iter_)
print(Border)

#--------------------------------------------------------
# Step 13. Training Accuracy
#--------------------------------------------------------

print(Border)
print("Step 13.Training Accuracy")
print(Border)

Y_train_pred = model.predict(X_train_scaled)

print("Training accuracy :\n", accuracy_score(Y_train, Y_train_pred))
print(Border)

#--------------------------------------------------------
# Step 14.Testing Accuracy
#--------------------------------------------------------

print(Border)
print("Step.14Testing Accuracy")
print(Border)

Y_test_pred = model.predict(X_test_scaled)
print("Testing accuracy : \n", accuracy_score(Y_test,Y_test_pred))
print(Border)

#--------------------------------------------------------
# Step 15.Confusion matrix
#--------------------------------------------------------

print(Border)
print("Step 15.Confusion matrix")
print(Border)

Y_pred = model.predict(X_test_scaled)

cm = confusion_matrix(Y_test, Y_pred)

print("Confusion metrix :\n", cm)

display = ConfusionMatrixDisplay(confusion_matrix=cm)
display.plot()

plt.show()
print(Border)

#--------------------------------------------------------
# Step 16. Loss curve
#--------------------------------------------------------

print(Border)
print("Step 16. Loss curve")
print(Border)

plt.plot(model.loss_curve_)

plt.title("Training loss curve")
plt.xlabel("Iteration")
plt.ylabel("Loss")

plt.show()
print(Border)

#--------------------------------------------------------
# Step 17. Test system
#--------------------------------------------------------

def PredictAttrition(employe_data):
    print(Border)
    print("Step 17. Test system")
    print(Border)
    
    employe_data_scaled= scaler.transform(employe_data)
    
    prediction = model.predict(employe_data_scaled)
    
    print("Employee Attrition Prediction:")
    print(Border)

    for i, prediction in enumerate(prediction, start=1):

        if prediction == 1:
            print(f"Employee {i}: Attrition = Yes (Employee may leave)")
        else:
            print(f"Employee {i}: Attrition = No (Employee may stay)")
    
#--------------------------------------------------------
# Step 18. Model performance analysis
#--------------------------------------------------------
    print(Border)
    print("Step 18. Model performance analysis")
    print(Border)

    print("1.Training Accuracy: The model achieved 82.57% accuracy on training data.\n"
      "2.Testing Accuracy: The model achieved 77.33% accuracy on unseen testing data.\n"
      "3.Accuracy Difference: The difference is 5.24%, which is relatively small.\n"
      "4.Overfitting: Since training accuracy is higher than testing accuracy, the model shows slight overfitting, but it is not severe.\n"
      "5.Underfitting: The model is not underfitting because both training and testing accuracies are reasonably good.\n"
      "6.Confusion Matrix: The model predicts No Attrition better than Yes Attrition. It correctly identifies 218 No-Attrition cases but only 14 Yes-Attrition cases.\n"
      "7.Conclusion: Overall, the model has reasonable performance with slight overfitting and needs improvement in identifying employees who are likely to leave the company.")


def main():
    employe_data = pd.DataFrame({
        'Age': [25, 35, 45, 30, 50],
        'MonthlyIncome': [30000, 60000, 80000, 45000, 100000],
        'YearsAtCompany': [2, 8, 15, 5, 20],
        'TotalWorkingYears': [3, 10, 20, 7, 25],
        'DistanceFromHome': [5, 15, 10, 25, 8],
        'JobSatisfaction': [3, 4, 2, 3, 4],
        'WorkLifeBalance': [3, 4, 2, 3, 4],
        'OverTime': [1, 0, 1, 0, 1],
        'NumCompaniesWorked': [1, 2, 3, 1, 4],
        'TrainingTimesLastYear': [2, 3, 1, 4, 2]
    })
    
    PredictAttrition(employe_data)
    
if __name__ =="__main__":
    main()


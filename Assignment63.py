import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix , classification_report
#------------------------------------------ 
# Step 1. Load dataset 
#------------------------------------------
Border = '-'*40
print(Border)
print("Step 1. Load dataset ")
print(Border)

df = pd.read_csv("Loan_Default.csv")

print(df.head())

#------------------------------------------ 
# Step 2. EDA (Exploratory Analysis)
#------------------------------------------

print(Border)
print("Step 2. EDA (Exploratory Analysis)")
print(Border)

print("Shape of Dataset :", df.shape)

print("Total Records :", df.shape[0])
print("Total Columns :", df.shape[1])
print(Border)

print("Summary Statistics :\n", df.describe())

#------------------------------------------ 
# Step 3. Missing values 
#------------------------------------------

print(Border)
print("Step 3. Missing values ")
print(Border)
 
print("Missing values :", df.isnull().sum())

#------------------------------------------ 
# Step 4. Check target class balanced
#------------------------------------------

print(Border)
print("Step 4. Check target class balanced")
print(Border)
 
print("Traget class distribution")
class_counts = df['Default'].value_counts()
print(class_counts)

ratio = class_counts.min() / class_counts.max()

if ratio < 0.5:
    print("Conclusion: Target classes are IMBALANCED.")
else:
    print("Conclusion: Target classes are reasonably BALANCED.")
    
print(Border)

#------------------------------------------ 
# Step 5. Encode Categorial variable
#------------------------------------------

print(Border)
print("Step 5. Encode Categorial variable")
print(Border)

LE = LabelEncoder()

df['PreviousDefault'] = LE.fit_transform(df['PreviousDefault'])

df['HomeOwnership'] = LE.fit_transform(df['HomeOwnership'])

print(df.head())
print(Border)

#------------------------------------------ 
# Step 6. Separate X and Y
#------------------------------------------

print(Border)
print("Step 6. Separate X and Y")
print(Border)

X = df.drop(['Default'] , axis=1)
Y = df['Default']

print("Shape of X :", X.shape)
print("Shape of Y :", Y.shape)
print(Border)

#------------------------------------------ 
# Step 7. Split the dataset into training and testing
#------------------------------------------

print(Border)
print("Step 7. Split the dataset into training and testing")
print(Border)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.30, random_state=42, stratify=Y)

print("Divide dataset sucessfully")

#------------------------------------------ 
# Step 8.Stratified Split
#------------------------------------------

print(Border)
print("Step 8.Stratified Split")
print(Border)

print("""Stratified splitting is used because Default is a
classification target variable.
It maintains the same proportion of class 0 and class 1
in both training and testing datasets.""")

print(Border)

#------------------------------------------ 
# Step 9.Scale the features 
#------------------------------------------

print(Border)
print("Step 9.Scale the features ")
print(Border)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)

print("Scaled Training data")
print(X_train_scaled[:5])

#------------------------------------------ 
# Step 10. Create an MLPclassifier
#------------------------------------------

print(Border)
print("Step 10. Create an MLPclassifier")
print(Border)

model = MLPClassifier(
    hidden_layer_sizes=(32,16),
    activation='relu',
    solver="adam",
    max_iter=1000,
    random_state=42
)

#------------------------------------------ 
# Step 11. Train the Model
#------------------------------------------

print(Border)
print("Step 11. Train the Model")
print(Border)

model.fit(X_train_scaled,Y_train)

print("Model Training Completed Successfully")

#------------------------------------------ 
# Step 12. Calculate accuracy
#------------------------------------------

print(Border)
print("Step 12. Calculate accuracy")
print(Border)

Y_train_pred = model.predict(X_train_scaled)
print("Training accuracy :\n", accuracy_score(Y_train, Y_train_pred))

Y_test_pred = model.predict(X_test_scaled)
print("Testing accuracy : \n", accuracy_score(Y_test,Y_test_pred))

print(Border)

#------------------------------------------ 
# Step 13. Confusion matrix
#------------------------------------------

print(Border)
print("Step 13. Confusion matrix")
print(Border)

cm = confusion_matrix(Y_test, Y_test_pred)

print("Confusion matrix :\n",cm)

print(Border)

#------------------------------------------ 
# Step 14. classification report
#------------------------------------------

print(Border)
print("Step 14. classification report")
print(Border)

report = classification_report(Y_test, Y_test_pred)
print(report)

#------------------------------------------ 
# Step 15. Plot training loss curve
#------------------------------------------

print(Border)
print(" Step 15. Plot training loss curve")
print(Border)

plt.plot(model.loss_curve_)

plt.title("Training loss curve")
plt.xlabel("Iteration")
plt.ylabel("Loss")

plt.show()

#------------------------------------------ 
# Step 16. Test the model
#------------------------------------------

new_data = pd.DataFrame({
    'Age': [25, 45, 35, 55, 30],

    'Income': [300000,750000,450000, 900000,250000],

    'LoanAmount': [500000,200000,700000,300000,800000],

    'CreditScore': [600, 750, 550, 800, 500],

    'EmploymentYears': [2, 15, 5, 25, 1],

    'ExistingLoans': [2, 1, 3, 0, 4],

    'MonthlyDebt': [25000,10000,40000,5000,50000],

    'LoanTerm': [36, 24, 48, 12, 60],

    'PreviousDefault': [0, 0, 1, 0, 1],
    'HomeOwnership': [1, 0, 1, 0, 1]
})

new_data_scaled = scaler.fit_transform(new_data)

prediction = model.predict(new_data_scaled)

print("Loan Default Prediction: \n", prediction)

for i, prediction in enumerate(prediction, start=1):

        if prediction == 1:
            print(f"Customer {i}: Default = Yes (May default on loan)")
        else:
            print(f"Customer {i}: Default = No (May not default on loan)")


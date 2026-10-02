import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.neural_network import MLPClassifier
#-----------------------------------------
# Step 1 : Load or create dataset
#-----------------------------------------

Border = "-"* 40
print(Border)
print(" Step 1 : Load or create dataset")
print(Border)

# Features:
# [Age, Monthly Charges, Tenure, Complaints, Support Calls]

X = np.array([
    [25,500,12,1,2],
    [30,700,24,0,1],
    [45,1200,6,5,8],
    [50,1500,5,6,10],
    [28,600,18,1,1],
    [35,800,30,0,0],
    [48,1400,4,7,9],
    [52,1600,3,8,12],
    [27,550,20,0,1],
    [42,1300,8,4,7]
])

Y =np.array ([
    0,0,1,1,0,
    0,1,1,0,1
])

print("Dataset loaded sucsesfully")

#-----------------------------------------
# Step 2: Split the dataset
#-----------------------------------------
print(Border)
print(" Step 2 : Split the Dataset")
print(Border)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, random_state=42, train_size=0.8)

print("Training Input Shape : ", X_train.shape)
print("Testing Input Shape : ", X_test.shape)
print("Training Output Shape : ", Y_train.shape)
print("Testing Output Shape : ", Y_test.shape)

#-----------------------------------------
# Step 3: Apply StandardScalar
#-----------------------------------------
print(Border)
print("Step 3: Apply StandardScalar ")
print(Border)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# --------------------------------------------------
# STEP 4: Create and Train FNN
# --------------------------------------------------
print(Border)
print("STEP 4: Create and Train FNN ")
print(Border)

model = MLPClassifier(
    hidden_layer_sizes=(8,),
    activation='relu',
    solver='lbfgs',
    max_iter=5000,
    random_state=42
)

model.fit(X_train, Y_train)


# --------------------------------------------------
# STEP 5: Evaluate Accuracy
# --------------------------------------------------
print(Border)
print(" STEP 5: Evaluate Accuracy")
print(Border)

y_pred = model.predict(X_test)

accuracy = accuracy_score(Y_test, y_pred)

print("Model Accuracy:", accuracy * 100, "%")


# --------------------------------------------------
# STEP 6: Test New Customer
# --------------------------------------------------
print(Border)
print("STEP 6: Test New Customer")
print(Border)

new_customer = np.array([
    [46, 1450, 5, 6, 9]
])

new_customer_scaled = scaler.transform(new_customer)

prediction = model.predict(new_customer_scaled)[0]

# --------------------------------------------------
# STEP 7: Display Result
# --------------------------------------------------
print(Border)
print("STEP 7: Display Result")
print(Border)

if prediction == 1:
    print("Prediction: Customer may leave")
else:
    print("Prediction: Customer may stay")
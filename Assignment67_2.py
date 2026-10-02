# ============================================================
# Neural Network Model for Loan Approval Prediction
# ============================================================

import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report


# ------------------------------------------------------------
# 1. Dataset
# Features:
# [Income, Credit Score, Loan Amount, Existing EMI, Employment Status]
#
# Employment Status:
# 0 = Not Stable
# 1 = Stable
# ------------------------------------------------------------

X = np.array([
    [25000, 600, 200000, 10000, 0],
    [40000, 700, 300000,  8000, 1],
    [60000, 750, 500000, 12000, 1],
    [20000, 550, 150000, 15000, 0],
    [80000, 800, 700000, 10000, 1],
    [35000, 650, 250000,  9000, 1],
    [18000, 500, 100000, 12000, 0],
    [90000, 850, 800000, 15000, 1],
    [30000, 580, 200000, 14000, 0],
    [70000, 780, 600000, 10000, 1]
])

# Output:
# 0 = Loan Rejected
# 1 = Loan Approved

y = np.array([
    0, 1, 1, 0, 1,
    1, 0, 1, 1, 0
])

# ------------------------------------------------------------
# 2. Split dataset into training and testing data
# ------------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# ------------------------------------------------------------
# 3. Feature Scaling
# Neural networks work better when numerical features
# are on a similar scale.
# ------------------------------------------------------------

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# ------------------------------------------------------------
# 4. Create Neural Network (FNN) Model
#
# hidden_layer_sizes=(10, 5)
#   First hidden layer  = 10 neurons
#   Second hidden layer = 5 neurons
#
# activation = ReLU
# max_iter   = maximum training iterations
# ------------------------------------------------------------

model = MLPClassifier(
    hidden_layer_sizes=(10, 5),
    activation='relu',
    solver='adam',
    max_iter=2000,
    random_state=42
)

# ------------------------------------------------------------
# 5. Train the Neural Network
# ------------------------------------------------------------

model.fit(X_train, y_train)

# ------------------------------------------------------------
# 6. Evaluate the Model
# ------------------------------------------------------------

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("======================================")
print("       LOAN APPROVAL PREDICTION")
print("======================================")

print("\nModel Accuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report:")
print(classification_report(
    y_test,
    y_pred,
    target_names=["Loan Rejected", "Loan Approved"],
    zero_division=0
))

# ------------------------------------------------------------
# 7. Predict for a New Applicant
#
# Income          = 55000
# Credit Score    = 720
# Loan Amount     = 400000
# Existing EMI    = 10000
# Employment      = 1 (Stable)
# ------------------------------------------------------------

new_applicant = np.array([
    [55000, 720, 400000, 10000, 1]
])

new_applicant_scaled = scaler.transform(new_applicant)

prediction = model.predict(new_applicant_scaled)

# ------------------------------------------------------------
# 8. Display Prediction
# ------------------------------------------------------------

print("\n======================================")
print("         NEW APPLICANT")
print("======================================")

if prediction[0] == 1:
    print("Prediction: Loan Approved")
else:
    print("Prediction: Loan Rejected")
    

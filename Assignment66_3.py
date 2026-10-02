import numpy as np

# Mean Squared Error
def mean_squared_error(actual, predicted):
    return np.mean((actual - predicted) ** 2)

# Binary Cross Entropy
def binary_cross_entropy(actual, predicted):

    # Avoid log(0)
    predicted = np.clip(predicted, 1e-15, 1 - 1e-15)

    loss = -(actual * np.log(predicted) +
             (1 - actual) * np.log(1 - predicted))

    return np.mean(loss)

# Actual values
actual = np.array([1, 0, 1, 1, 0])

# Predicted values
predicted = np.array([0.9, 0.2, 0.8, 0.7, 0.1])

# Calculate MSE
mse = mean_squared_error(actual, predicted)

# Calculate Binary Cross Entropy
bce = binary_cross_entropy(actual, predicted)

# Display results
print("Actual Values    :", actual)
print("Predicted Values :", predicted)

print("\nMean Squared Error :", mse)
print("Binary Cross Entropy :", bce)
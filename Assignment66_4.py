# Python program to show how weights are updated in an ANN

# 1. Take input values
x = float(input("Enter input: "))
w = float(input("Enter weight: "))
b = float(input("Enter bias: "))
target = float(input("Enter target output: "))
learning_rate = float(input("Enter learning rate: "))

# Store old weight
old_weight = w

# 2. Calculate prediction
prediction = (x * w) + b

# 3. Calculate error
error = target - prediction

# 4. Update weight using gradient descent
# Gradient = (prediction - target) * input
gradient = (prediction - target) * x

new_weight = w - (learning_rate * gradient)

# 5. Display results
print("\n--- ANN Weight Update ---")
print("Prediction      :", prediction)
print("Target Output   :", target)
print("Error           :", error)
print("Old Weight      :", old_weight)
print("Gradient        :", gradient)
print("Updated Weight  :", new_weight)
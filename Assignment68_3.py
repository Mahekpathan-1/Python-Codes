# Program to demonstrate Flattening

# 1. Take a 2D matrix
matrix = [
    [6, 4],
    [8, 6]
]

print("Input Matrix:")
for row in matrix:
    print(row)

# 2. Convert 2D matrix into 1D vector
flatten_output = []

for row in matrix:
    for value in row:
        flatten_output.append(value)

print("\nFlattened Output:")
print(flatten_output)

# 3. Pass flattened vector to a Fully Connected Layer

weights = [1, 2, 1, 2]
bias = 1

# 4. Calculate final output manually using:
# Output = (x1*w1) + (x2*w2) + (x3*w3) + (x4*w4) + bias

output = 0

for i in range(len(flatten_output)):
    output = output + (flatten_output[i] * weights[i])

output = output + bias

print("\nWeights:")
print(weights)

print("Bias:")
print(bias)

print("\nFinal Output:")
print(output)
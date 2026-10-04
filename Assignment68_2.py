import numpy as np

#######################################
# Step 1: Create 5*5 image
#######################################

image = np.array([
    [0,0,0,0,0],
    [0,0,0,0,0],
    [1,1,1,1,1],
    [0,0,0,0,0],
    [0,0,0,0,0]
])

print("\nOriginal 6x6 image")
print(image)

#######################################
# Step 2: 3*3 kernel 
#######################################

Kernel = np.array([
    [-1,-1,-1],
    [0,0,0],
    [1,1,1]
])

print("\n3x3 kernel")
print(Kernel)

#######################################
# Step 3 : Convolutinal operation
#######################################


feature_map = np.zeros((3,3))

for i in range(3):
    for j in range(3):
        
        # Extract 3x3 region
        region = image[i:i+ Kernel.shape[0], j:j+Kernel.shape[1]]
        
        # Multiply and Sum
        result = np.sum(region * Kernel)
        
        # Store result
        feature_map[i][j] = result
        
#######################################
# Step 4 : Show feature map
#######################################

print("\n Feature map (Detected edge)")
print(feature_map)

#######################################
# Step 5: Aplly ReLU
#######################################

ReLU = np.maximum(0,feature_map)

print("\nAfter ReLU:")
print(ReLU)


#######################################
# Step 6: Apply 2x2 Max Pooling
#######################################

pool_size = 2

output_rows = ReLU.shape[0] - pool_size + 1
output_cols = ReLU.shape[1] - pool_size + 1

pool_output = np.zeros((output_rows, output_cols))

for i in range(output_rows):

    for j in range(output_cols):

        # Extract 2x2 region
        region = ReLU[
            i:i + pool_size,
            j:j + pool_size
        ]

        # Find maximum value
        pool_output[i][j] = np.max(region)


#######################################
# Step 7: Display Final Output
#######################################

print("\nAfter 2x2 Max Pooling:")
print(pool_output)
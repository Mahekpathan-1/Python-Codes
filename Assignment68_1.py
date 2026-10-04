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


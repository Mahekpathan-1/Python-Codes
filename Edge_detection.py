#--------------------------------------
# 6x6 Grayscale Image
# Top Half = Black (0)
# Bottom Half = White(255)
# Apply 3x3 kernel for edge Detection
# Show Feature Map
#--------------------------------------

import numpy as np

#--------------------------------------
# step 1. Create 6x6 Image
#--------------------------------------

image = np.array([
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [255,255,255,255,255,255],
    [255,255,255,255,255,255],
    [255,255,255,255,255,255]
    ])

print("\nOriginal 6x6 Image")
print(image)

#--------------------------------------
# step 2. 3x3 Kernel for Horizontal Edge Detection
#--------------------------------------

Kernel = np.array([
    [-1, -1, -1],
    [ 0,  0,  0],
    [ 1,  1,  1]
])

print("\n3x3 Kernel")
print(Kernel)

#--------------------------------------
# step 3. Convolution operation
#--------------------------------------

feature_map = np.zeros((4,4))

for i in range(4):
    for j in range(4):
        
        # Extract 3x3 region
        region = image[i:i+3, j:j+3]
        
        # Multiply and Sum
        result = np.sum(region * Kernel)
        
        # Store result
        feature_map[i][j] = result
        
#--------------------------------------
# step 4. Show Feature Map
#--------------------------------------
        
print("\nFeature map (Detected Edge)")
print(feature_map)

import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Read Image
img = cv2.imread("sample.png")

# 2. Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 3. Display image + grid

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(gray, cmap="gray")

plt.title("Grayscale Image")
plt.axis("off")
plt.subplot(1,2,2); plt.imshow(gray, cmap="gray")

plt.colorbar(label = "Pixel value")
plt.title("Pixel values")

plt.show()
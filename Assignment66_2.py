import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp((-x)))

def ReLU(x):
    return np.maximum(0,x)

def tanh(x):
    return np.tanh(x)

x = np.linspace(-10, 10, 100)
    
sigmoid_out = sigmoid(x)
ReLU_out = ReLU(x)
tanh_out = tanh(x)
    
plt.plot(x, sigmoid_out)
plt.title("Sigmoid Activation Function")
plt.xlabel("Input")
plt.ylabel("Output")
plt.grid()
plt.show()

plt.plot(x, ReLU_out)
plt.title("ReLU Activation Function")
plt.xlabel("Input")
plt.ylabel("Output")
plt.grid()
plt.show()

plt.plot(x, tanh_out)
plt.title("Tanh Activation Function")
plt.xlabel("Input")
plt.ylabel("Output")
plt.grid()
plt.show()
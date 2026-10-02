import numpy as np
import math

def Sigmoid(z):
    return 1 / (1 + math.exp(-z))

def marvellous():
       
    input = np.array([2,3])
    print("X :", input)

    weights = np.array([0.4,0.6])
    print("W :", weights)

    bias = 0.5
    print("b :", bias)

    z = np.dot(input, weights) + bias
    print("Weighted sum :", z)
    
    y = Sigmoid(z)
    
    return y

def main():
    
    result = marvellous()
    
    print("predicted result :", result)
    
    if result >= 0.5:
       print("Class 1 : Output close to 1")
    else:
       print("Class 0 : Output close to 0")
    
if __name__ =="__main__":
    main()



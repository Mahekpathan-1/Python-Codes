from functools import reduce

Minimum = lambda No1 , No2 : (No1 if No1< No2 else No2)

def main():
    
    Data = [ 23, 67, 12, 3, 45, 1]
    
    RData = reduce(Minimum, Data)
    
    print("Input Data : ", Data)
    
    print("Minimum number is :", RData)
    
if __name__ == "__main__":
    main()
from functools import reduce

Maximum = lambda No1, No2 : No1 if No1> No2 else No2 

def main():
    
    Data = [ 23, 67, 12, 3, 45, 1]
    
    RData = reduce(Maximum , Data)
    
    print("Input Data :", Data)
    
    print("Maximum number is :", RData)
    
if __name__ == "__main__":
    main()
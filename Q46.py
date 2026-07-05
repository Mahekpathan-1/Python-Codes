from functools import reduce

Addition = lambda No1 , No2 : No1 + No2

def main():
    
    Data = [ 12, 34, 50, 23]
    
    RData = (reduce(Addition,Data))
    
    print("input data :",Data)
    
    print("Addition is :", RData)
    
if __name__ == "__main__":
    main()
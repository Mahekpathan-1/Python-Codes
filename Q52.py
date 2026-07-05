EvenCount = lambda No : (No % 2 == 0)

def main():
    
    Data = [ 20,10,4,5,39,55,40,23]
    
    FData = list(filter(EvenCount, Data))
    
    Count= len(FData)
    
    print("Input Data is :", Data)
    
    print("Even Number is :", FData)
    
    print("Count of Even number is :", Count)
    
if __name__ == "__main__":
    main()    
    
    
    

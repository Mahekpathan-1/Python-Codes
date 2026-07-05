OddNo = lambda No : (No % 2 !=0)

def main():
    
    Data =  [13,12,8,10,20,19,64]
    
    FData = list(filter(OddNo,Data))
    
    print("Input Data is :", Data)
    
    print("Odd number is :", FData)
    
if __name__ == "__main__":
    main()
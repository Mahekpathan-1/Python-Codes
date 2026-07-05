EvenNo = lambda No : (No % 2 == 0)

def main():
    
    Data = [13,12,8,10,20,19,64]
    
    FData = list(filter(EvenNo,Data))
    
    print("Input Data is :", Data)
    
    print("Even number is :", FData)
    
if __name__ == "__main__":
    main()
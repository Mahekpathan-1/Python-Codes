CheckDivisible = lambda Number  : Number % 3 == 0 and Number % 5 == 0

def main():
    
    Data = [ 6, 10, 12 ,8, 9, 30, 15, 20, 18, 1 , 45]
    
    FData = list(filter(CheckDivisible,Data))
    
    print("Input Data :", Data)
    
    print("Number Is Divisible both 3 and 5 :",FData )
    
if __name__ == "__main__":
    main()
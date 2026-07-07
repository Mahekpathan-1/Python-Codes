def CountDigit(No):
    Count = 0
    
    while No > 0:
        Count += 1
        No = No //10
    return Count
        
def main():
    
    value = int(input("Enter a Number :"))
    Ans = CountDigit(value)
    
    print("Number of digits is :", Ans)
    
if __name__ =="__main__":
    main()
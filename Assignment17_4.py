def AddFact(No):
    Sum = 0
    
    for i in range(1, No):
        if No % i == 0:
            Sum = Sum + i
            
    return Sum
    
def main():
    value = int(input("Enter a number :"))
    Ans = AddFact(value)
    
    print("Addition of Factorial is :", Ans)
    
    
if __name__ == "__main__":
    main()
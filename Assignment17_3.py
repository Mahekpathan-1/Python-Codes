def Fact(No):
    Fact = 1
    
    for i in range(1, No+1):
        Fact = Fact * i
    return Fact
    
def main():
    
    value = int(input("Enter a number :"))
    Ans = Fact(value)
    
    print("Factorial is :", Ans)
    
    
if __name__ == "__main__":
    main()
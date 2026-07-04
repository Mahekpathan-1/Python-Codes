Maximum = lambda No1 , No2 : No1 if No1>No2 else No2

def main():
    value1 = int(input("enter first number : "))
    value2 = int(input("enter second number : "))
    
    Ret = Maximum(value1, value2)
    
    print("Maximum number is :", Ret)
    
    
if __name__ == "__main__":
    main()
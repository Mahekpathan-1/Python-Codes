def Sumdigit(No):
    Sum = 0
    
    while No > 0:
        digit = No % 10
        Sum = Sum + digit
        No = No // 10
    return Sum
    
def main():
    
    value = int(input("Enter a number :"))
    Ans = Sumdigit(value)
    print("Addition is :", Ans)
    
if __name__ == "__main__":
    main()
# Accept two parameters and return multiplication 
# Input: 4 3
# output : 12

Multiplication = lambda No1 , No2 : No1 * No2

def main():
    
    value1 = int(input("Enter first number :"))
    value2 = int(input("Enter second number :"))
    
    Ans = Multiplication(value1, value2)
    
    print("Multiplication is :", Ans)
    
if __name__ == "__main__":
    main()
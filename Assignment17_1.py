import Arithmetic

def main():
    
    num1 = int(input("Enter First Number :"))
    num2 = int(input("Enter Second number :"))
    
    print("Addition is :", Arithmetic.Add(num1, num2))
    
    print("Substraction is :", Arithmetic.Sub(num1, num2))
    
    print("Multiplication is :", Arithmetic.Mult(num1, num2))
    
    print("Division is :", Arithmetic.Div(num1, num2))
    
if __name__ == "__main__":
    main()
def Arithmetic(No1, No2):
    print("Addition is : ", No1 + No2)
    print("substraction is :", No1 - No2)
    print("Multiplication is :", No1 * No2)
    print("Division is :", No1 / No2)
    
def main():
    value1 = int(input("enter first number : "))
    value2 = int(input("enter second number : "))
    
    Arithmetic(value1, value2)
    
if __name__ == "__main__":
    main()
    


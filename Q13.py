def Multiplication_Table(num):
    for i in range(1,11):
        print(num * i )

def main():
    Value = int(input("Enter a number : "))
    Multiplication_Table(Value)

if __name__ =="__main__":
    main()
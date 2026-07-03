def ChkGreater(a,b):
    if a > b :
        print("Greater number is :", a)
    elif b > a:
        print("greater number is :", b)
    else:
        print("Both are Equal")
        
def main():
    no1 = int(input("enter first number:"))
    no2 = int(input("enter second number:"))
    
    ChkGreater(no1,no2)

if __name__== "__main__":
    main()

    
def Chknum(No):
    
    if No % 2 == 0 :
        print("Even Number")
    else:
        print("Odd Number")
    
    
def main():
    
    num= int(input("Enter a number : "))
    
    Ret = Chknum(num)
    

if __name__ == "__main__":
    main()
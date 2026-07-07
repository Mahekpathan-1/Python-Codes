def ChkNumber(No):
    
    if No > 0:
        print("Number is Positive ")
        
    elif No < 0:
        print("Number is Negative ")
    
    else:
        print("Zero")
        
    
def main():
    num = int(input("Enter A Number : "))
    Result = ChkNumber(num)
    
if __name__ == "__main__":
    main()
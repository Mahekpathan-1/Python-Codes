Odd = lambda No : True if No % 2 !=0 else False

def main():
    
    value = int(input("Enter A Number :"))
    
    Result = Odd(value)
    
    print(Result)
    
if __name__== "__main__":
    main()
Div = lambda No : True if No % 5 == 0 else False

def main():
    
    value = int(input("Enter a number :"))
    
    Result = Div(value)
    
    print(Result)
    
if __name__ == "__main__":
    main()
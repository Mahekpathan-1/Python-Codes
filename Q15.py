def Factorial(num):
    fact = 1
    i = 1
    
    while i<= num:
        fact = fact * i
        i = i + 1
    print("factorial is :", fact)
        
def main():
    value = int(input("Enter a Number:"))
    
    Factorial(value)


if __name__ == "__main__":
    main()    
    

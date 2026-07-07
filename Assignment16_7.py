def Divisible(num):
    
    return num % 5 == 0
    
def main():
    
    value = int(input("Enter a Number :"))
    
    Result = Divisible(value)
    
    if Result:
        print("True")
    else:
        print("False")
    
if __name__ == "__main__":
    main()
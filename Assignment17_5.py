def ChkPrime(No):
    Count = 0
    
    for i in range(1,No+1):
        if No % i == 0:
            Count += 1
            
    if Count == 2:
        return True
    else:
        False
        
    
def main():
    
    value = int(input("Enter Number :"))
    
    if ChkPrime(value):
        print("It is prime number")
    else:
        print("it is not prime number")
    
    
if __name__ == "__main__":
    main()
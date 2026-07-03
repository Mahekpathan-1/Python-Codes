def Sumof(num):
    Sum = 0
    i = 1
    
    while i <= num:
        Sum = Sum + i
        i = i + 1
        
    print("sum of natural number is :", Sum)
        
def main():
    value = int(input("Enter a Number : "))
    Sumof(value)
    
if __name__ == "__main__":
    main()
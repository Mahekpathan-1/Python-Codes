def Odd(num):
    for i in range(1 , num + 1, 2):
        print(i)
    
def main():
    value = int(input("Enter a number:"))
    
    Odd(value)
    
if __name__ == "__main__":
    main()
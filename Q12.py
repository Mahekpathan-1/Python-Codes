def Div(num):
    if num % 3 == 0 and num % 5 == 0:
        print("number is Divisible by 3 and 5")
        
    else:
        print("number is not divisible by 3 and 5 ")
        
def main():
    value = int(input("Enter Number:"))
    Div(value)

if __name__ == "__main__":
    main()       

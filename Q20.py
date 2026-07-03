def Reverse(No):
    Rev = 0
    
    while No > 0:
        digit = No % 10
        Rev = Rev * 10 + digit
        No  = No // 10
        
    print("Reverse number:", Rev)
    
def main():
    num = int(input("Enter a Number:"))
    Reverse(num)
    
if __name__ == "__main__":
    main()
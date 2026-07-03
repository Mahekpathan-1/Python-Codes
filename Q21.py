def CheckPalindrome(No):
    Temp = No
    Rev = 0
    
    while No > 0:
        digit = No % 10
        Rev = Rev * 10 + digit 
        No = No // 10
        
    if Temp == Rev :
        print("palindrome")
    else:
        print("not palindrome")
        
def main():
    num = int(input("Enter a Number:"))
    CheckPalindrome(num)
    
if __name__ =="__main__":
    main()
        

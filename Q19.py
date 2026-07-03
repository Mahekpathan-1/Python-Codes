def SumDigits(No):
    sum = 0
    
    while No >0:
        digit = No % 10
        sum = sum + digit 
        No = No // 10
        
    print("sum of digits is :", sum)
    
def main():
    num = int(input("Enter a number:"))
    SumDigits(num)
    
if __name__ =="__main__":
    main() 
        
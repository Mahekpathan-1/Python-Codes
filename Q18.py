def countdigit(No):
    count = 0
    
    while No > 0:
        count = count + 1
        No = No // 10
        
    print("Count of digits :", count)
    
def main():
    num = int(input("Enter A Number:"))
    
    countdigit(num)
    
if __name__ == "__main__":
    main()
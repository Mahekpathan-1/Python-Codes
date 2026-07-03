def Even(num):
    
    for i in range(2 , num + 1, 2):
        print(i)
        
def main():
    value = int(input("Enter a Number:"))
    
    Even(value)
    
if __name__ =="__main__":
    main()
    
    
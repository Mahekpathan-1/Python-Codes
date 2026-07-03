def CheckPerfect(No):
    
    sum = 0
    
    for i in range(1,No):
        if No % i == 0:
            sum +=i
            
    if sum == No :
        return True
    else:
        return False
    
def main():
    
    value = int(input("Enter a Number : "))
    CheckPerfect(value)
    
    if CheckPerfect(value):
        print("Perfect number is : ", value)
    else:
        print("not perfect number")
        
if __name__ == "__main__":
    main()
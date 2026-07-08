# Accept one parameter and return power of two
# input :4
# output : 16

Power = lambda No : No ** 2

def main():
    
    value = int(input("Enter number :"))
    
    Result = Power(value)
    
    print("Power of two is :", Result)
    
if __name__ =="__main__":
    main() 
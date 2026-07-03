def AreaOfRectangle(Length, width):
    
    Area = Length * width
    
    return Area 

def main():
    
    value1 = int(input("Enter the Lenght : "))
    value2 = int(input("Enter the Width : "))
    
    Ret = AreaOfRectangle(value1 , value2 )
    
    print("Area of Rectangle : ", Ret)    
    
if __name__ == "__main__":
    main()
    
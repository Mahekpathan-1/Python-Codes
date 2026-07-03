def AreaOfCircle(radius):
    
    Area = 3.14 * radius * radius
    return Area

def main():
    
    value = int(input("Enter Radius : "))
    
    Ret = AreaOfCircle(value)
    
    print("Area of circle is : ", Ret)
    
if __name__ == "__main__":
    main()
def Displaygrade(Marks):
    
    if Marks >=75:
        print("Destination")
    
    elif Marks >= 60:
        print("First class")
        
    elif Marks >= 50:
        print("second Class")
        
    else:
        print("fail")
        
def main():
    
    value = int(input("Enter Marks : "))
    
    Displaygrade(value)
    
if __name__ == "__main__":
    main()
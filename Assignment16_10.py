def Namelength(name):
    
    return len(name)
    
def main():
    
    StrName = input("Enter Name :")
    Result = Namelength(StrName)
    
    print("Length of name is :", Result)
    
if __name__ == "__main__":
    main()
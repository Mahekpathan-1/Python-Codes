def Display(No):
    
    for i in range(No):
        print("*" , end = "  ")
    
    
def main():
    
    value = int(input("Enter a number : "))
    Ret = Display(value)
    
if __name__ == "__main__":
    main()
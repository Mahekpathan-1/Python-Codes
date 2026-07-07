def Display(No):
    
    for i in range(No, 0, -1):
        for j in range(i):
            print("*", end = " ")
        print()
    
def main():
    
    value = int(input("Enter a number :"))
    Display(value)
    
if __name__ == "__main__":
    main()
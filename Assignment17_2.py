def Display(No):
    
    for i in range(No):
        for j in range(No):
            print("*", end = " ")
        print()
    
def main():
    
    value = int(input("Enter A number :"))
    Display(value)
    
if __name__ == "__main__":
    main()
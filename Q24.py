def printfactors(No):
    for i in range(1, No + 1):
        if No % i == 0:
            print(i)
            
def main():
    num= int(input("Enter A Number:"))
    printfactors(num)
    
if __name__ == "__main__":
    main()
        
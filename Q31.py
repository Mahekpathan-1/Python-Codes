def BinaryEquivalent(No):
    binary = ""

    while No > 0:
        remain = No % 2
        binary = str(remain) + binary 
        No = No // 2

    print("Binary equivalent is :",binary)

def main():
    
    Value = int(input("Enter the Number : "))
    BinaryEquivalent(Value)

   
if __name__ == "__main__":
    main()
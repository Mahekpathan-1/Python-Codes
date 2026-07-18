class Numbers:
    
    def __init__(self, Value):
        self.Value = Value 
        
    def ChkPrime(self):
        if self.Value < 2:
            return False

        for i in range(2, self.Value):
            if self.Value % i == 0:
                return False

        return True
    
    def ChkPerfect(self):
        Sum = 0

        for i in range(1, self.Value):
            if self.Value % i == 0:
                Sum = Sum + i

        return Sum == self.Value

    def Factors(self):
        print("Factors of", self.Value, "are:")

        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")

        print()

    def SumFactors(self):
        Sum = 0

        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                Sum = Sum + i

        return Sum
    
def main():

    print("Enter first number:")
    No1 = int(input())

    print("Enter second number:")
    No2 = int(input())

    Obj1 = Numbers(No1)
    Obj2 = Numbers(No2)

    print("\n----- First Object -----")
    print("Number:", Obj1.Value)

    print("Is Prime:", Obj1.ChkPrime())
    print("Is Perfect:", Obj1.ChkPerfect())

    Obj1.Factors()

    print("Sum of Factors:", Obj1.SumFactors())

    print("\n----- Second Object -----")
    print("Number:", Obj2.Value)

    print("Is Prime:", Obj2.ChkPrime())
    print("Is Perfect:", Obj2.ChkPerfect())

    Obj2.Factors()

    print("Sum of Factors:", Obj2.SumFactors())


if __name__ == "__main__":
    main()



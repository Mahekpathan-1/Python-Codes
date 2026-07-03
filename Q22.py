def CheckPrime(No):
    if No <= 1:
        print("Not Prime")
        return

    for i in range(2, No):
        if No % i == 0:
            print("Not Prime")
            return

    print("Prime Number")


def main():
    Num = int(input("Enter Number : "))
    CheckPrime(Num)

if __name__ == "__main__":
    main()
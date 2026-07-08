# Accept N number from user store it in list
# input : 13 5 45 7 4 56
#output :130

from functools import reduce

def Addition(No1,No2):
    return No1+No2

def main():
    Elements = int(input("Enter Number of elements :"))
    
    value = list(map(int,input("Enter Numbers :").split()))
    
    Result = reduce(Addition,value)
    print(Result)
    
if __name__ == "__main__":
    main()
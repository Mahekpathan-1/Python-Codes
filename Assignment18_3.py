# Accept N number from user stored in list. return minimum number
#input :13 5 45 7
#output : 5

from functools import reduce

Minimum = lambda No1 , No2 :  No1 if No1 < No2 else No2
    
def main():
    
    Elements = int(input("Enter Number of elements :"))
    
    value = list(map(int,input("Enter number :").split()))
    
    Result = reduce(Minimum, value)
    
    print("Minimum number is :", Result)
    
    
if __name__ == "__main__":
    main()
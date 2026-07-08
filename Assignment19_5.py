# Filter - prime number
# Map - multiply each number by 2
# Reduce - maximum number 
# Input - [2,70,11,10,17,23,31,77]
# list after filter = [2,11,17,23,31]
# list after map = [4,22,34,46,62]
# output of reduce = 62

from functools import reduce

def ChkPrime(No):
    
    if No <= 1:
        return False
    
    for i in range(2, No):
        if No % i ==0:
            return False
    
    return True

def Mult(No):
    return No * 2 

def Maximum(No1,No2):
    if No1>No2:
        return No1
    else:
        return No2
    
def main():
    value = list(map(int,input("Enter numbers :").split()))
    
    FData = list(filter(ChkPrime,value))
    print("list after filter :",FData)
    
    MData = list(map(Mult,FData))
    print("list after map :",MData)
    
    RData = reduce(Maximum,MData)
    print("Maximum number is :", RData)

if __name__ == "__main__":
    main()    
    
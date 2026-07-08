# Filter - Even number
# Map - calculate square
# Reduce - addition of numbers
# Input :[5,2,3,4,3,4,1,2,8,10]
# list after filter : [2,4,4,2,8,10]
# list after map :[4, 16,16,4,64,100]
# output of reduce : 204

from functools import reduce

ChkEven = lambda No :  No % 2 == 0
Square = lambda No : No ** 2
Addition = lambda No1, No2 : No1 + No2 

def main():
    
    Value = list(map(int,input("Enter numbers : ").split()))
    
    FData = list(filter(ChkEven,Value))
    print("list after filter :", FData)
    
    MData = list(map(Square,FData))
    print("list after map :", MData)
    
    RData = reduce(Addition,MData)
    print("Addition is :",RData)
    
if __name__ == "__main__":
    main()
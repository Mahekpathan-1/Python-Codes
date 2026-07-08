# Filter - greater than or equal to 70 and less than or equal to 90
# Map - increase each number by 10 
# Reduce - product of all numbers 
# Input List = [ 4, 34,36,76,68,24,89,23,86,90,45,70]
# List After filter = [76,89,86,90,70]
# List after map = [86,99,96,100,80]
# Output of reduce = 6538752000

from functools import reduce

chkNo = lambda No : No >= 70 and No<=90

Increment = lambda No : No + 10 

Product = lambda No1, No2 : No1 * No2

def main():
    
    value = list(map(int,input("Enter Numbers :").split()))
    
    FData = list(filter(chkNo,value))
    print("List after filter :",FData)
    
    MData = list(map(Increment,FData))
    print("List after map :", MData)
    
    RData = reduce(Product,MData)
    print("output of reduce :",RData)
    
if __name__ == "__main__":
    main()
    
    
    
    
# Accept N numbers from users and stored list. return maximum number
#input = 13 5 45 7 4 56 34
#output = 56

from functools import reduce

def Maximum(No1, No2):
    
    if No1 > No2 :
        return No1
    else:
        return No2
    
def main():
    Elements = int(input("Enter number of elements :"))
    
    value = list(map(int,input("Enter numbers :").split()))
    
    Result = reduce(Maximum , value)
    
    print("Maximum number is :", Result)
    
if __name__ == "__main__":
    main()
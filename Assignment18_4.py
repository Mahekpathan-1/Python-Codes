# Accept N number from user and store it into list . Accept one another number from 
# user and return frequency of that number from list
#input :11
#Input elements : 13 5 45 7 4 56 5 34 2 5 65
#Element to search : 5
#output : 3


def main():
    
    Elements = int(input("Enter number of elemnts :"))
    
    value = list(map(int,input("Enter number :").split()))
    
    Search = int(input("Enter number to search :"))
    
    Result = len(list(filter(lambda No : No == Search, value)))
    
    print("Frequency is :", Result)
    
if __name__  == "__main__":
    main()
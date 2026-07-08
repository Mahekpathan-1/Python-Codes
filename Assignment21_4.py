import threading

def Fun(Data):
    sum= 0
    for i in Data:
        sum = sum + i
    print("sum of elements :",sum)
    
def product(Data):
    
    Result = 1
    
    for i in Data:
        Result = Result * i
    print("Product of elements is :", Result)
    
def main():
    
    Data = list(map(int,input("Enter elements :").split()))
    
    T1 = threading.Thread(target = Fun, args=(Data,))
    T2 = threading.Thread(target = product, args=(Data,))
    
    T1.start()
    T2.start()
    
if __name__ == "__main__":
    main()
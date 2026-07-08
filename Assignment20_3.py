import threading

def EvenList(Data):
    Sum= 0
    
    print("Even elements are :")
    for i in Data:
        if i % 2 == 0:
            print(i)
            Sum = Sum + i
    print("Sum off Even elements :", Sum)
    
def oddList(Data):
    Sum = 0
    
    print("Odd elements are :")
    for i in Data:
        if i % 2 !=0:
            print(i)
            Sum = Sum + i
    print("sum of odd elements :", Sum)
    
def main():
    
    value = int(input("Enter number of elements :"))
    Data =list(map(int,input("Enter elements  :").split()))
    
    t1 = threading.Thread(target = EvenList, args=(Data,))
    t2 = threading.Thread(target = oddList, args=(Data,))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    

if __name__ == "__main__":
    main()
    
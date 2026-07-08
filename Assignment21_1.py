import threading

def ChkPrime(No):
    
    if No < 2:
        return False
    for i in range(2,No):
        if No % i == 0:
            return False
        
    return True

def Prime(Data):
    print("Prime Numbers: ")
    
    for i in Data:
        if ChkPrime(i):
            print(i)
            
def Nonprime(Data):
    print("Nonprime Numbers :")
    
    for i in Data:
        if ChkPrime(i) == False:
            print(i)
        
def main():
    
    Data = list(map(int,input("Enter numbers:").split()))
    
    t1 = threading.Thread(target = Prime, args=(Data,))
    t2 = threading.Thread(target = Nonprime, args=(Data,))

    t1.start()
    t1.join()
    
    t2.start()
    t1.join()
    
if __name__ =="__main__":
    main()
        
import threading

def Maximum(Data):
    
    print("Maximum number is :",max(Data))
    
def Minimum(Data):
    
    print("Minimum number is :",min(Data))

def main():
    
    Data = list(map(int,input("Enter numbers :").split()))
    
    t1 = threading.Thread(target = Maximum, args= (Data,))
    t2 = threading.Thread(target = Minimum, args= (Data,))
    
    t1.start()
    t2.start()
    
if __name__ == "__main__":
    main()
    
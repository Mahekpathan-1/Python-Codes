import threading

def Thread1():
    print("number from 1 to 50 :")
    for i in range(1,51,1):
        print(i)
        
def Thread2():
    print("Number from 50 to 1:")
    for i in range(50,0,-1):
        print(i)
        
def main():
    
    t1 = threading.Thread(target = Thread1)
    t2 = threading.Thread(target = Thread2)
    
    t1.start()
    t1.join()
    
    t2.start()
    t2.join()
    
if __name__ == "__main__":
    main()
import threading

def Small(string):
    count = 0
    
    for ch in string:
        if ch.islower():
            count = count + 1
        
    print("Thread id :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("number of lowercase character:", count)
    print()
    
def Capital(string):
    
    count = 0
    
    for ch in string:
        if ch.isupper():
            count = count + 1
            
    print("Thread id :",threading.get_ident())
    print("Thread name :", threading.current_thread().name)
    print("Number of uppercase character :",count)
    print()
    
def Digits(string):
    
    count = 0
    
    for ch in string:
        if ch.isdigit():
            count = count + 1
            
    print("Thread id :", threading.get_ident())
    print("Thread name :", threading.current_thread().name)
    print("Number of digits:", count)
    print()
    
def main():
    
    value = input("Enter string :")
    
    t1 = threading.Thread(target= Small, args=(value,))
    t2 = threading.Thread(target = Capital, args=(value,))
    t3 = threading.Thread(target= Digits, args=(value,))
    
    t1.start()
    t1.join()
    
    t2.start()
    t2.join()
    
    t3.start()
    t3.join()
    
if __name__ == "__main__":
    main()
        
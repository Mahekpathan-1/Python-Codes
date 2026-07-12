from multiprocessing import Pool
import os

def CountPrime(No):
    print("PID is :", os.getpid())
    count = 0
    
    for i in range(2,No+1):
        Flag = True
        
        for j in range(2,i):
            if j % i == 0:
                Flag = False
                
            if Flag == True:
                count = count + 1 
    return count
    
def main():
    
    Data = list(map(int,input("Enter Numbers :").split()))
    
    P = Pool()
    
    Result = P.map(CountPrime,Data)
    
    P.close()
    P.join()
    
    for value,Ans in zip(Data,Result):
        print(f"Prime numbers between 1 to ", value, "=", Ans)
            
if __name__ == "__main__":
    main()
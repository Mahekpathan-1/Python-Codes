# accept list of integers and uses Pool.map()to calculate the sum of sqaures from 1 to N
# input = [1000000,2000000,3000000,40000001]

from multiprocessing import Pool
import os
import time

def SumSquare(No):
    print("PID is :", os.getpid())
    Sum = 0
    
    for i in range(1,No+1):
        Sum = Sum + (i * i )
    return Sum 

def main():
    start_time = time.perf_counter()
    
    Data = list(map(int,input("Enter Numbers :").split()))
    
    P = Pool()
    result = P.map(SumSquare,Data)
    
    P.close()
    P.join()
    
    print(result)
    
    end_time = time.perf_counter()
    
    print("Execution time is :", end_time-start_time)
    
if __name__ == "__main__":
    main()

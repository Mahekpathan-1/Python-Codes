# calculate 1^5 + 2^5 + 3^5 + 4^5+...N^5 for multiplr values of n using pool
# measure total execution time

import multiprocessing
import os
import time

def Calculate(num):
    total = 0
    
    for i in range(1,num+1):
        total = total + i**5
        
    return total

def main():
    Data = list()
    size = int(input("Enter number of elements :"))
    
    for i in range(1, size+1):
        no = int(input(f"Enter {i} element :"))
        Data.append(no)
        
    start_time = time.perf_counter()
    
    pobj = multiprocessing.Pool()
    
    Ret = list(pobj.map(Calculate,Data))
    
    pobj.close()
    pobj.join()
    
    print(Ret)

    end_time = time.perf_counter()
    
    print(f"time required for execution is : {end_time-start_time:.4f} seconds")
    
if __name__ =="__main__":
    main()
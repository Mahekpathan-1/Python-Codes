# Calculate factorials of multiple numbers simultaneously using Pool.map()
# input = [10,15,20,25]
#Display = Process Id, Input Number, Factorial

from multiprocessing import Pool
import os

def Factorial(No):
    print("PID is :",os.getpid())
    
    Fact = 1
    for i in range(1 , No+1):
        Fact = Fact * i
    return Fact

def main():
    
    Data = list(map(int,input("Input Numbers :").split()))
    
    P = Pool()
    
    result = P.map(Factorial,Data)
    
    P.close()
    P.join()
    
    print("factorial is :", result)
    
if __name__ == "__main__":
    main()
        
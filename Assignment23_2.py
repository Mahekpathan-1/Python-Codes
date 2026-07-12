from multiprocessing import Pool
import os
import time


def SumOdd(Number):
    """
    Calculate the sum of all odd numbers from 1 to Number.
    """

    Total = 0

    for i in range(1, Number + 1, 2):
        Total = Total + i

    return (os.getpid(), Number, Total)


def main():

    Data = [1000000, 2000000, 3000000, 4000000]

    print("Input Data :", Data)
    print("-" * 50)

    Start = time.time()

    P = Pool()

    Result = P.map(SumOdd, Data)

    P.close()
    P.join()

    End = time.time()

    for PID, Number, Total in Result:
        print(f"Process ID        : {PID}")
        print(f"Input Number      : {Number}")
        print(f"Sum of Odd Numbers: {Total}")
        print("-" * 50)

    print("Total Execution Time :", End - Start, "seconds")


if __name__ == "__main__":
    main()
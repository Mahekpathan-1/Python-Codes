from multiprocessing import Pool
import os
import time


def CountEven(Number):
    """
    Count even numbers from 1 to Number.
    """

    Count = 0

    for i in range(2, Number + 1, 2):
        Count = Count + 1

    return (os.getpid(), Number, Count)


def main():

    Data = [1000000, 2000000, 3000000, 4000000]

    print("Input Data :", Data)
    print("-" * 50)

    Start = time.time()

    P = Pool()

    Result = P.map(CountEven, Data)

    P.close()
    P.join()

    End = time.time()

    for PID, Number, Count in Result:
        print(f"Process ID        : {PID}")
        print(f"Input Number      : {Number}")
        print(f"Even Number Count : {Count}")
        print("-" * 50)

    print("Total Execution Time :", End - Start, "seconds")


if __name__ == "__main__":
    main()
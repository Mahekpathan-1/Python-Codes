from multiprocessing import Pool
import os
import time


def Factorial(Number):
    """
    Calculate factorial of a number.
    """

    Fact = 1

    for i in range(1, Number + 1):
        Fact = Fact * i

    return (os.getpid(), Number, Fact)


def main():

    Data = [10, 15, 20, 25]

    print("Input Data :", Data)
    print("-" * 50)

    Start = time.time()

    P = Pool()

    Result = P.map(Factorial, Data)

    P.close()
    P.join()

    End = time.time()

    for PID, Number, Fact in Result:
        print(f"Process ID   : {PID}")
        print(f"Input Number : {Number}")
        print(f"Factorial    : {Fact}")
        print("-" * 50)

    print("Total Execution Time :", End - Start, "seconds")


if __name__ == "__main__":
    main()
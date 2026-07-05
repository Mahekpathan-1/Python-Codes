Sqaure = lambda No : No * No

def main():
    Data = [1,2,3,4,5,6,7,8]
    
    MData = list(map(Sqaure,Data))
    
    print("original list :", Data)
    
    print("Sqaure is :", MData)
    
if __name__ == "__main__":
    main()
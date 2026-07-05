Stringlen = lambda X : len (X) > 5

def main():
    
    Data = [ "Python", "Programming ", "Language", " code", "process", "C", "Java", "C#"]
    
    FData = list(filter(Stringlen, Data))
    
    print("Input Data :", Data)
    
    print("String Greater than 5 :", FData)
    
if __name__ =="__main__":
    main()
#Accept a file name, open the file, and display its complete contents on the console
import os

def main():
    
    FileName = input("Enter file name :")
    fobj = open(FileName,"r")
    
    Data = fobj.read()
    
    print("Contents of",FileName, "are:")
    print(Data)
    
if __name__ == "__main__":
    main()
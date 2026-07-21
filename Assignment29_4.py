#Accept an existing file name through command-line arguments, create a new file named Demo.txt, and copy all contents into it.
import os
import sys

def main():
    
    File1 = sys.argv[1]
    File2 = sys.argv[2]
    
    if not os.path.exists(File1):
        print(File1,"does not exist")
        return
    if not os.path.exists(File1):
        print(File1,"does not exist")
        return
    
    fobj = open(File1,"r")
    Data1= fobj.read()
    fobj.close()
    
    fobj = open(File2,"r")
    Data2 = fobj.read()
    fobj.close()
    
    if Data1 == Data2:
        print("Success")
    else:
        print("Failure")
    
if __name__ == "__main__":
    main()
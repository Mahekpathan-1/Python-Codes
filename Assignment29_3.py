#Accept an existing file name through command-line arguments, create a new file named Demo.txt, and copy all contents into it.

import os
import sys

def main():
    
    SourceFile = sys.argv[1]
    if len(sys.argv) != 2:
        print("Invalid number of arguments")
        return
    
    if os.path.exists(SourceFile):
        print("File is exists")
    else:
        print("File not exists")
        
    fobj = open(SourceFile,"r")
    Data = fobj.read()
    fobj.close()
    
    fobj = open("Demo.txt", "w")
    Data = fobj.write(Data)
    fobj.close()
    
if __name__ == "__main__":
    main()
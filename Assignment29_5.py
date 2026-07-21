#Accept a file name and a string from the user, then count how many times that string appears in the file.

import os

def main():
    
    FileName = input("Enter File Name :")
    SearchString = input("Enter string :")
    
    fobj = open(FileName , "r")
    
    count = 0
    
    for line in fobj:
        words = line.split()
        
        for word in words:
            if word == SearchString:
                count = count +1
                
    fobj.close()
    
    print(SearchString,"appears",count,"times in", FileName)
    
if __name__ == "__main__":
    main()
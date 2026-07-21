#Accept a file name from the user and check whether it exists in the current directory
import os

def main():
    
    FileName = input("Enter File Name :")
    
    Ret = os.path.exists(FileName)
    
    if(Ret == True):
        print(FileName,"exists in current directory")
        
    else:
        print(FileName,"Does not exists in current directory")
    
if __name__ == "__main__":
    main()
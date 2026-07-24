# program that reads and displays the contents of a specified text file every  minute.
# File does not exist
# FIle is empty
# Permission is denied
# File cannot be opened

import os
import schedule
import time

def Display(FileName):
    try:
        
       fobj = open(FileName,"r")
       
       print("_"*40)
       print("File Contents")
       print("_"*40)
       
       Data = fobj.read()
       
       if Data == " ":
           print("File is empty")
       else:
           print(Data)
           
       fobj.close()
       
    except FileNotFoundError:
        print("Error : File does not exists ")
        
    except PermissionError:
        print("Error : permision is denied")
        
    except OSError:
        print("Error : File not found error")
        
def main():
    
    FileName = input("Enter File name :")
    
    schedule.every(1).minutes.do(Display,FileName)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
        
if __name__ =="__main__":
    main()
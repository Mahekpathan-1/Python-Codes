# monitors the size of a specified file every 30 seconds
# File Path
# FIle Size in bytes
# Date and time 
# situation handle where the file does not exist

import os
import schedule
import datetime
import time

def Display(FileName):
    if os.path.exists(FileName):
    
       Filesize = os.path.getsize(FileName)
       Currenttime = time.ctime()

        
       fobj= open("Demo.txt","a")
       fobj.write("File Name :"+ FileName + "\n")
       fobj.write("File size in bytes :" +str(Filesize) +"bytes\n")
       fobj.write("Date and time :" + Currenttime + "\n")
    
       fobj.close()
       print("Succesfully run")
       
    else:
        print("File doesnot exists")
    
def main():
    FileName = input("Enter file path :")
    
    schedule.every(30).seconds.do(Display,FileName)
    
    while True:
        schedule .run_pending()
        time.sleep(1)
    
if __name__ == "__main__":
    main()
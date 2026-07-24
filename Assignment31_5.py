# program that accepts directory name from the user and counts the number of files inside it every five minute
# Directory path
# Number of files
# Date and Time

import os
import schedule
import datetime
import time

def DirectoryCount(Directorypath):
    
    FileCount = 0
    timestamp = time.ctime()
    
    for FolderName, SubFolderName,FileName in os.walk(Directorypath):
        FileCount = FileCount + len(FileName)
        
        fobj= open("DirectoryCountLog.txt","w")
        fobj.write("Directory Name :"+ Directorypath +"\n")
        fobj.write("Total number of Files :"+ str(FileCount) +"\n")
        fobj.write("Date and time :"+ timestamp+"\n")
        
        fobj.close()
        
    print("Directory scanned successfully")
    
def main():
    print("Automation script started")
    
    DirectoryName = input("Enter Directory name :")
    
    schedule.every(2).seconds.do(DirectoryCount,DirectoryName)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
        
if __name__ == "__main__":
    main()
        
        
        
# Scans a specified directory every minutr
# task should display
# Directory name
# Number  of files
# Number of subdirectories 
# Date and time of scanning

import os
import datetime
import schedule
import time

def DirectoryScanner(Directorypath):
    
    FileCount = 0
    DirectoryCount = 0
    currentTime = datetime.datetime.now()
    
    for FolderName,SubFolderName,FileName in os.walk(Directorypath):
        FileCount = FileCount + len(FileName)
        
        DirectoryCount = DirectoryCount + len(SubFolderName)
        
    print("_"*40)
    print("Directory Name :", Directorypath)
    print("Total number of files:",FileCount)
    print("Total number of subdirectories :",DirectoryCount)
    print("Date and time of scanning :", currentTime)
    print("_"*40)
    
def main():
    
    Directorypath = input("Enter Directory name : ")
    
    DirectoryScanner(Directorypath)
    
    schedule.every(1).minute.do(DirectoryScanner)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
        
if __name__ == "__main__":
    main()
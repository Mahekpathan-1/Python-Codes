# file backup every hour
# Accept the source file path
# Accept the destination directory path
# copy the source file to the destination directory
# Add the current date and time to the backup filename
# write the backup operation details into backup_log.txt

import os
import shutil
import datetime
import schedule
import time

def BackupFile(SourceFile, DestinationDirectory):
    currentTIme = datetime.datetime.now()
    
    FileName = os.path.basename(SourceFile)
    
    TimeStamp = currentTIme.strftime("%d_%m_%y_%H_%M_%S")
    
    BackupFileName =("Backup" + TimeStamp + "_" + FileName)
    
    DestinationPath = os.path.join(DestinationDirectory, BackupFileName)
    
    shutil.copy( SourceFile , DestinationPath)
    
    print("Backup completed ")
    print("Backup File :", BackupFileName)
    
    
def main():
    SourceFile = input("Enter source FIle Path :")
    
    DestinationDirectory = input("Enter destination directory path :")
    
    schedule.every(1).hour.do(BackupFile,SourceFile,DestinationDirectory)
    
    BackupFile(SourceFile , DestinationDirectory)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
        
if __name__ =="__main__":
    main()
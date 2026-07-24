# program that copies all .txt files from one directory to another every ten minutes and maintains a log of copied files.
# Accept source and destination directories
# validate both directories
# copy only .txt files
# maintain a log of copied files
# avoid terminating if one file cannot be copied 

import os
import schedule
import time
import shutil

def CopyFile(SourceDirectory,DestinationDirectory):
    
    LogFileName = "CopiedFiles.log"
    
    try:
        LogFileName = open(LogFileName,"a")
        print("scanning Source Directory ...")
        
        for FolderName,SubFolderName,FileName in os.walk(SourceDirectory):
            for Fname in FileName:
                if Fname.endswith(".txt"):
                    SourcePath = os.path.join(FolderName,Fname)
                    DestinationPath = os.path.join(DestinationDirectory,Fname)
                    
                    try:
                        shutil.copy(SourcePath,DestinationPath)
                        
                        print("Copied:", SourcePath)
                        
                        LogFileName.write(f"Copied:{SourcePath}"f"to{DestinationPath}\n")
                        
                    except Exception as Error:
                        print(f"unable to copy{SourcePath}")
                        print(f"REason: {Error}")
                        
                        continue
            LogFileName.close()
            print("Copied operation Completed")
            
    except Exception as error:
        print("Error while opening log File")
        print("Reason:",Error)
        
def main():
    
    SourceDirectory = input("Enter Source Directory:")
    DestinationDirectory = input("Enter Destination Directory:")
    
    
    if not os.path.exists(SourceDirectory):
        print("Source Directory deos not present")
        return
    
    if not os.path.isdir(SourceDirectory):
        print("Source Path is not a directory")
        return
    
    if not os.path.exists(DestinationDirectory):
            print("Destination Directory deos not present")
            return
        
    if not os.path.isdir(DestinationDirectory):
            print("Destination Path is not a directory")
            return
        
    schedule.every(10).minutes.do(CopyFile,SourceDirectory,DestinationDirectory)
        
    while True:
        schedule.run_pending()
        time.sleep(10)

if __name__ == "__main__":
    main()
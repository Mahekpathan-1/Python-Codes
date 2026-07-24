# Program that creates a new log file after every ten minutes
# Filename should contain the current date and time

import os
import time
import schedule

def DirectoryScanner(DirectoryPath = "Marvellous" ):
    
    timestamp = time.ctime()
    
    LogFileName = "Marvellous%s.log"%(timestamp)
    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")
    
    
    print("Log file gets created with name :", LogFileName)
    print("Creation Time :",timestamp)
    
    fobj = open(LogFileName,"w")
    
    fobj.write("Log file created successfully")

    fobj.close()
    
def main():
    
    print("Log file get created successfully")
    
    schedule.every(10).minutes.do(DirectoryScanner)
     
    while True:
         schedule.run_pending()
         time.sleep(1)
         
if __name__=="__main__":
    main()     
    
    
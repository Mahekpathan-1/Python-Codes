# program that creates a new txt file every minute
# filename should contain the current timestamp
# FIlename
# Creation date
# Creation time

import os
import schedule
import datetime
import time

def Display():
     
    timestamp = time.ctime()
    LogFileName = "Marvellous%s.log"%(timestamp)
    LogFileName = LogFileName.replace(":","_")
    LogFileName = LogFileName.replace(" ","_")
    
    fobj= open(LogFileName , "w")
    fobj.write("Filename :"+ LogFileName + "\n")
    fobj.write("Creation date:"+ time.strftime("%d:%m:%y \n"))
    fobj.write("Creation time :"+ time.strftime("%H:%M:%S"))
    
    fobj.close()
    
def main():
    
    schedule.every(1).seconds.do(Display)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
        
if __name__ =="__main__":
    main()
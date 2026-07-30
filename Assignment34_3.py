#Design an automation script that displays information about all running processes:
# Process Name
# PID
# Username

import time
import os
import sys
import psutil
import schedule

def ProcessScan():
    ListProcess = []
    
    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=["pid","name","username"])
        
        ListProcess.append(info)
        
    return ListProcess
        
def CreateLog(FolderName):
    
    Border = "_"*70
    
    Ret = False
    
    Ret = os.path.exists(FolderName)
    if(Ret == True):
        Ret = os.path.isdir(FolderName)
        if(Ret == False):
            print("unable to directory execute there is no directory ")
            
    else:
        os.mkdir(FolderName)
        print("Directory is created succesfully")
   
    timestamp = time.strftime("%Y_%m_%d-%H_%M_%S")
    
    FileName = ("Marvellous_%s.log" %timestamp)
    
    print(f"File is created with name {FileName}")
    
    FilePath = os.path.join(FolderName, FileName)
    
    fobj = open(FilePath , "w")
    
    fobj.write(Border + "\n\n")
    
    fobj.write("Information Of Running Processes\n")    
    
    fobj.write(Border + "\n\n")
    
    # Process info
    Data = ProcessScan()
    
    for info in Data:
        
        fobj.write("PID : %s\n" %info.get("pid"))
        fobj.write("Name : %s\n" %info.get("name"))
        fobj.write("Username : %s\n" %info.get("username"))
        fobj.write(Border + "\n")
        
    fobj.write(Border + "\n")
    fobj.write("----------------End of Log File---------------\n")
    fobj.write(Border + "\n")
    
    
    fobj.close()
def main():
    
    Border = "_"*70
    
    ProcessScan()
    
    if(len(sys.argv )== 2):
        if(sys.argv[1] == "--H" or sys.argv[1] == "--h"):
            print("This automation script is used to information of running processes")
            print("For better usage plz check --u flag")
            
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("please execute the script as ")
            print("python FileName.py DirectoryName")
            
        else:
            FolderName = sys.argv[1]

            schedule.every(10).seconds.do(CreateLog , FolderName)
            
            while True:
                schedule.run_pending()
                time.sleep(1)            
    else:
        print("Invalid number of arguments")
            
        
if __name__ == "__main__":
    main()
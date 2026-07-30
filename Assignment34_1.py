import time
import os
import psutil


def ProcessScan():
    
    listProcess = []
    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=["pid","name","username"])
        
        listProcess.append(info)
    return listProcess
    
def main():
    Border = "_"*60
    
    Data = ProcessScan()
    for info in Data:
            
        print("PID : %s\n" %info.get("pid"))
        print("Name : %s\n" %info.get("name"))
        print("Username : %s\n" %info.get("username"))
        print(Border + "\n")

if __name__ == "__main__":
    main()
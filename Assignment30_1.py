import os
import time
import schedule

def Display():
    print("Jay Ganesh......")

def main():
    
    print("Automation script start")
    
    schedule.every(2).seconds.do(Display)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
        
    print("End of Automation Scriptc")
    
    
if __name__ == "__main__":
    main()
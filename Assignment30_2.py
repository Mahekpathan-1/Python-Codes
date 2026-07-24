# Program that displays the current date and time every one minute

import os
import time
import schedule
import datetime

def Display():
    print("Current Date and Time : ", datetime.datetime.now())
    
def main():
    print("Automation script start")
    
    schedule.every(1).minute.do(Display)
    
    while True:
        schedule.run_pending()
        time.sleep(10)
    
    print("Automation script end")
    
if __name__ == "__main__":
    main()
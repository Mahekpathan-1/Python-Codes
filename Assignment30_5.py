# task that executes every five minutes
# task should contain current date and time into a file
# new entries should be append without removing previous entries

import schedule
import time
import datetime

def Display():
    currenttime = datetime.datetime.now()
    
    Filename = open("marvellous.txt", "a")
    
    Filename.write("Task executed at :" + str(currenttime) +"\n")
    
    Filename.close()
    
def main():
    print("Automation script start")
    
    schedule.every(5).seconds.do(Display)
    
    print("Data is append successfully")
    
    while True:
        schedule.run_pending()
        time.sleep(1)
        
if __name__=="__main__":
    main()
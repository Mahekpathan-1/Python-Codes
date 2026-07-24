# program that schedules a finction to print Coding Kar...!

import time
import schedule

def Function():
    print("Coding Kar....!")
    
def main():
    
    print("Automation script start")
    
    schedule.every(30).minutes.do(Function)
    
    while True:
        schedule.run_pending()
        time.sleep(10)
        
    print("End of automation script")
    
if __name__ =="__main__":
    main()
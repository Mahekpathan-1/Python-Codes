# print Lunch time ! every day at 1:00 pm
# print wrap up work every day at 6:00 pm

import schedule
import time
import datetime

def Fun1():
    print("Lunch Time!")
    
def Fun2():
    print("Wrap up Work")
    
def main():
    
    print("Automation script started")
    
    schedule.every().day.at("13:00").do(Fun1)
    schedule.every().day.at("18:00").do(Fun2)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
        
if __name__ == "__main__":
    main()
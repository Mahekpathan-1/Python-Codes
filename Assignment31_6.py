# schedule the message

import os
import schedule
import datetime
import time

def MondayMessage():
    print("start your weekly goals ")
    
def Wednesdaymessage():
    print("Review your weekly progress")
    
def FridayMessage():
    print("weekly work completed")
    
def main():
    
    schedule.every().monday.at("09:00").do(MondayMessage)
    schedule.every().wednesday.at("17:00").do(Wednesdaymessage)
    schedule.every().friday.at("18:00").do(FridayMessage)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
    
if __name__ == "__main__":
    main()
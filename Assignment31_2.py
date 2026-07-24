# create function  named:
# DisplayMessage(message)
# the message should be accepted from the user 

import schedule
import time

def DisplayMessage(Message):
    print(Message)
    
def main():
    
    Message = input("Enter message : ")
    
    schedule.every(5).seconds.do(DisplayMessage,Message)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
        
if __name__ =="__main__":
    main()
# Accept message from the user
# Accept time interval in seconds
# schedule program to display the message repeatedly after the specified interval 
# validate that the interval is greater than zero

import schedule
import time

def Display(Message):
    print(Message)
    
def main():
    
     Message = input("Enter Message : ")
     Interval = int(input("Enter interval in seconds :"))
     
     if Interval <= 0:
         print("Invalid Interval")
         return
     
     schedule.every(Interval).seconds.do(Display,Message)
     
     while True:
         schedule.run_pending()
         time.sleep(1)
         
if __name__ =="__main__":
    main()
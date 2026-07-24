# task that executes every day at 9:00 am and prints Namskar
import schedule
import time

def task():
    
    print("Namskar.....")
    
def main():
    print("Automation script started")
    
    schedule.every().day.at("09:00").do(task)
    
    while True:
        schedule.run_pending()
        time.sleep(30)
        
    print("Automation script end")
    
if __name__ == "__main__":
    main()
import psutil
import sys

def DisplayInformation(process_name):

    for proc in psutil.process_iter():
        info = proc.as_dict(attrs = ["pid" , "name" , "username"])

        if(process_name == proc.name()):

            print("Name : ",info["name"])
            print("PID : ",info["pid"])
            print("Username : ",info["username"])
            print("\n")

def main():
    if(len(sys.argv) == 2):
        DisplayInformation(sys.argv[1])
    else:
        print("Invalid argument")
        print("Please run the program as : ")
        print(f"{sys.argv[0]} process_name")
        
if __name__ =="__main__":
    main()
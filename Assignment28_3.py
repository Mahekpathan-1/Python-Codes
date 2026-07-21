#Accept a file name from the user and display the content of file line by line on screen.

def main():
    
    try:
        FileName = input("Enter File Name :")
        
        fobj = open(FileName, "r")
        
        print("File is opened")
        
        for Line in fobj:
            print(Line, end = "")
            
        fobj.close()
        
    except FileNotFoundError:
        print("File is not exists")
    
if __name__ == "__main__":
    main()
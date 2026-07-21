#Copy the contents of one existing file into a new file.
def main():
    
    try:
        SourceFile = input("Enter existing File Name :")
        DestinationFile = input("Enter new File Name :")
        
        fobj1 = open(SourceFile, "r")
        print("Source File gets opened")
        
        fobj2 = open(DestinationFile, "w")
        print("Destination File gets created")
        
        for Line in fobj1:
            fobj2.write(Line)
            
        print("Content copy sccessfully")
            
        fobj1.close()
        fobj2.close()
        
    except FileNotFoundError:
        print("Source file is not present")
    
if __name__ == "__main__":
    main()
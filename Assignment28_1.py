#Accept a file name from the user and count the total number of lines present in the file.
def main():
    
    try:
        FileName = input("Enter file name :")
        
        fobj = open(FileName, "r")
        
        print("file gets opened")
        
        Linecount = 0
        
        for Line in fobj:
            Linecount = Linecount + 1
            
        print("Total Number of Lines ", FileName, ":" ,Linecount)
        
        fobj.close()
        
    except FileNotFoundError:
        print("file is not exits")
    
if __name__ == "__main__":
    main()
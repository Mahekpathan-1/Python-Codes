#Accept a file name from the user and count the total number of words present in the file.

def main():
    try:
        FileName = input("Enter file Name :")
        
        fobj = open(FileName, "r")
        
        print("File gets opened")
        
        Wordcount = 0
        
        for line in fobj:
            
            words = line.split()
            
            Wordcount = Wordcount + len(words)
            
        print("Total number of words in ",FileName , ":",Wordcount)
        
        fobj.close()
    except FileNotFoundError:
        print("File is not eists")
    
if __name__ == "__main__":
    main()
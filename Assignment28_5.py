#Search whether a given word is present in a file or not
def main():
    
    try:
        FileName = input("Enter file name :")
        Searchword = input("Enter word to search :")
        
        fobj = open(FileName,"r")
        print("File gets opened")
        
        Found = False
        
        for Line in fobj:
            
            words = Line.split()
            
            if Searchword in words:
                Found = True
                break
            
        if Found == True:
                print( Searchword , "word is present in the file")
                
        else:
                print(Searchword ," is not present in the file")
                
                fobj.close()
                
    except FileNotFoundError:
        print("File is not exists")
        
if __name__ == "__main__":
    main()
# program that deletes all empty files from a specified directory every hour and maintains a log of deleted files.
# scan the directory recursively
# detect files whose size in zero bytes
# delete the empty files
# store deleted file paths in a log file
# handle permission errors

import os
import schedule
import time

def Empty(DirectoryPath):

    timestamp = time.ctime()

    Logfile = "marvellous%s.log" % (timestamp)

    Logfile = Logfile.replace(":", "_")
    Logfile = Logfile.replace(" ", "_")

    Ret = os.path.exists(DirectoryPath)

    if Ret == False:
        print("No such Directory is present")
        return

    Ret = os.path.isdir(DirectoryPath)

    if Ret == False:
        print("Given path is not a directory")
        return

    print("Logfile is created :", Logfile)

    fobj = open(Logfile, "w")

    fobj.write("Files from directory are:\n")

    TotalFiles = 0
    EmptyFiles = 0

    for FolderName, SubFolderName, FileName in os.walk(DirectoryPath):

        for fname in FileName:

            TotalFiles = TotalFiles + 1
            FilePath = os.path.join(FolderName, fname)
            
            FileSize = os.path.getsize(FilePath)

            fobj.write(f"{FilePath}: {FileSize} bytes\n")
            
            if FileSize == 0:

                EmptyFiles = EmptyFiles + 1

                os.remove(FilePath)

                print("Deleted :", FilePath)

    fobj.write( f"\nTotal scanned files : {TotalFiles}\n")

    fobj.write(f"Total empty or deleted files : {EmptyFiles}\n")

    fobj.close()


def main():

    DirectoryName = input("Enter Directory Name : ")

    schedule.every(1).seconds.do(Empty,DirectoryName)

    while True:
        schedule.run_pending()
        time.sleep(2)
        
if __name__ == "__main__":

    main()
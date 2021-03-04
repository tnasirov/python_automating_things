#!/bin/python3
import shutil    # For CopyFile
import os        # For getting file size and cheking if file exists
import sys       # For CLI args


# log-clean.py log.txt 10 5

if(len(sys.argv) < 4):
    print("Missing argumen! Usage is: Script name, Log name, log size and log file count")
    exit(1)
    
file_name  = sys.argv[1]
limitsize  = int(sys.argv[2])
logsnumber = int(sys.argv[3])

if(os.path.isfile(file_name)) == True:            # Check if log file exists
    logfile_size = os.stat(file_name).st_size     # Getting file size in Bytes
    logfile_size = logfile_size / 1024            # Converting into Kilobytes

if(logfile_size >= limitsize):                    # Check if actual logfile size is greater or equal to size we gave
    if(logsnumber > 0):                           # If given log file number is more than zero
        for currentFileNum in range(logsnumber, 1, -1): # We iterate from given logsnumber to 1 with -1
            src = file_name + "_" + str(currentFileNum-1) # we define source file 
            dst = file_name + "_" + str(currentFileNum)   # we defien dst file
            if(os.path.isfile(src) == True):        # Check if there is any file with src file number
                shutil.copyfile(src, dst)           # if yes copy source file as destination file
                print(f'Copied {src} to {dst} ')
        
        shutil.copyfile(file_name, file_name + "_1")  # rename our main file to file_1
        print(f'Copied {file_name} to {file_name}_1')
    
    myfile = open(file_name, 'w')                     # after all the files renamed, we open our main filan in write mode
    myfile.close()                                    # and it erases the file.
                
            
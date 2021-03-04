from urllib import request
import sys



myURL = "https://adv400.tripod.com/kartink.jpg"
myFile = "C:\\Users\\Tural_Nasirov\\Downloads\\kartinka.jpg"

try:
    print(f'Start download file from {myURL}')
    request.urlretrieve(myURL, myFile)
except Exception as e:
    print("Diqqet!!!")
    print(e)
    sys.exit()
    
    
print(f'File downloaded to the directory {myFile}')
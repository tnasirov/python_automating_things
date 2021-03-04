from urllib import request

myURL = "https://google.com"
answer = request.urlopen(myURL)

mytext1 = answer.readlines()
mytex2 = answer.read()

for i in mytext1:
    print(i)
#Problem-27 ---> Create a Log File with Timestamp --> Way -->2

from time import time,ctime
from math import floor
start =floor(time())
delay =3
while floor(time())-start < 3:
    pass

messageforFile = f"Hey This is python PS-27@v2 code.\nThe code i written in {ctime()}"
newText = open('hello2.txt','a')
newText.write(messageforFile)
print('File created with timestamp')

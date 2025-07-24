#Problem-27 ---> Create a Log File with Timestamp

from time import time
from math import floor
start =floor(time())
delay =3
while floor(time())-start < 3:
    pass

newText = open('hello.txt','a')
newText.write("Hello World \n I'm Py")
print(None)

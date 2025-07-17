# Problem-4-->Make Palindrome Checker 
# string check if it's a palindrome (same forward/backward).-- NaN=NaN , 

forwardStr =input('Enter a string for Reverse : ')
backwardStr = ''
i=0 
while i < len(forwardStr):
    backwardStr=forwardStr[i] + backwardStr
    i=i+1

if forwardStr ==backwardStr :
    print(f"{backwardStr} is a Palindrome Word")
else :
    print(f"{backwardStr} isn't a Palindrome Word")
    
# NaN is a Palindrome Word
# racecar is a Palindrome Word
# rotator is a Palindrome Word
# None isn't a Palindrome Word
# Hello isn't a Palindrome Word
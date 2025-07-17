# Problem -3 --> Resverse String Like -- Hello -> olleH

orginalStr =input('Enter a string for Reverse : ')
reverseStr = ' '
i=0 
while i < len(orginalStr):
    reverseStr=orginalStr[i] + reverseStr
    i=i+1
print(reverseStr)

# Rose -> esoR
# Python -> nohtyP
# Hello World -> dlroW olleH 
# john Doe -> eoD nhoj 
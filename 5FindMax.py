# Problem-5---> Find Max without using max();

numbers =[1,2,6,8,12,43]

maxNum =0
minNum =numbers[2]
i =0
while i<len(numbers):
    if numbers[i] > maxNum :
        maxNum=numbers[i]
    if numbers[i] < minNum:
        minNum = numbers[i]
    i=i+1
print(f"The Max Number is --> {maxNum}") #The Max Number is --> 43
print(f"The Min Number is --> {minNum}") #The Min Number is --> 1

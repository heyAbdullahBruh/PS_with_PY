# Problem -7 ---> Sum of Digits
# Input: 1234 → Output: 10 (1+2+3+4)

digits1 =[4,5,7,2,6,8,9,3,1,23,65,2]
digits2 =[14,35,57,72,886,98,99,43,21,213,625,23]
digits3 =[43,54,75,26,67,88,99,3,91,97,655,32]

def sumOfDigits (digitList):
    sum =0
    for n in digitList: 
        sum = n+sum
    print(sum)
sumOfDigits(digits1) #135
sumOfDigits(digits2) #2186
sumOfDigits(digits3) #1330


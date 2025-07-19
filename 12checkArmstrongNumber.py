#Problem -12 ---> Check Armstrong Number number --> 
# like -> 153 → has 3 digits ----> 1³ + 5³ + 3³ = 1 + 125 + 27 = 153 
# 9474 → has 4 digits---> 9⁴ + 4⁴ + 7⁴ + 4⁴ = 6561 + 256 + 2401 + 256 = 9474 

def checkArmstrongNum(number):
    numbToList = []
    for d in str(number):
        numbToList.append(d)
    sum =0 
    for dn in numbToList:
        sum = sum + (int(dn) ** len(numbToList))
    if sum == number :
        return True
    else: 
        return False

# checkArmstrongNum(534535)s

ArmstrongNums=[]
for i in range(1,1000001):
    if checkArmstrongNum(i) :
        ArmstrongNums.append(i)
print(ArmstrongNums) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 9474, 54748, 92727, 93084, 548834]
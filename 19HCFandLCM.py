# Problem-19 --> LCM and HCF 

# LCM -->
def LCM (num):
    result =[]
    for i in range(1,num+1):
        if num %i ==0:
            result.append(i)
    return result
# print(LCM(500)) #[1, 2, 4, 5, 10, 20, 25, 50, 100, 125, 250, 500]

# HCF -->
def HCF (numList):
    common = set(LCM(numList[0]))

    for n in numList[1:]:
        common&=set(LCM(n))
    return common
print(HCF([500,300,200]))

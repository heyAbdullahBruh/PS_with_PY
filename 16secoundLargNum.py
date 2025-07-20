#Promlem-16---> Find second largest numb from list ---> 

numList =[3,4,68,5,65,32,88]

# way ---> 1 
# def check2ndLargNum(listN) :
#     secLargNum=0
#     largeNum=0
#     for i in range(len(listN)):
#         if listN[i] > largeNum:
#             largeNum=listN[i]
#     for j in range(len(listN)):
#         if listN[j] > secLargNum and largeNum !=listN[j] :
#             secLargNum=listN[j]
#     return {"largeNum":largeNum,"secLargNum":secLargNum,}

# way ---> 2 
# def check2ndLargNum(listN) :
#     secLargNum=0
#     largeNum=0
#     for i in listN:
#         if i > largeNum:
#             largeNum=i
#     for j in listN:
#         if j > secLargNum and largeNum !=j :
#             secLargNum=j
#     return {"largeNum":largeNum,"secLargNum":secLargNum,}

# way---->3
def check2ndLargNum(listN) :
    secLargNum=0
    largeNum=0
    i=0
    while i < len(listN):
        if listN[i] > largeNum:
            largeNum=listN[i]
        elif listN[i] > secLargNum and largeNum !=listN[i] :
             secLargNum=listN[i]
        i=i+1
    return {"largeNum":largeNum,"secLargNum":secLargNum,}
print(check2ndLargNum(numList))


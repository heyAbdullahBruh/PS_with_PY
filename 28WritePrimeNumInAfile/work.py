#Problem-28 ---> Write Prime Numbers from 1–N to a File

def checkPrime(numb):
    if numb <=1 :
        return False
    for d in range(2,int(numb**.5)+1):
        if numb%d ==0:
            return False
    return True

def collectPrimeNum(timesNum):
    primeNums =[n for n in range(2,timesNum+1) if checkPrime(n)]
    return primeNums
    
primeNums2to100=collectPrimeNum(100)

primeNumsFile = open('primeNumsFile.txt','a')

for pn in primeNums2to100 :
    primeNumsFile.write(f'{pn}\n')

print("Done")
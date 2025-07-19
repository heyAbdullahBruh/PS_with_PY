# Problem -11 ---> Check prime number --> 

# number = int(input("Enter a number to check it prime ? : "))

def checkPrime(number) :
    if number == 0 or number == 1:
        print(f"{number} is not a prime number")
    if number == 2:
        print(f"{number} is a prime number")
    nums =[]
    i =2 
    while i<= number **.5 :
        nums.append(i)
        i=i+1
    for n in nums :
        if number % n ==0:
            print(f"{number} is not a prime number")
            return
    print(f"{number} is a prime number")
    
checkPrime(97)#97 is a prime number
checkPrime(17)#17 is a prime number  
checkPrime(9)#9 is not a prime number 
checkPrime(25)#25 is not a prime number 
checkPrime(93)#93 is not a prime number 
checkPrime(23)#93 is a prime number 

# Problem -11 ---> Check prime number --> 

# number = int(input("Enter a number to check it prime ? : "))

# Way --1 
def checkPrime(number) :
    if number <= 1:
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

#way -2 
def checkPrime2(number) :
    if number <= 1:
        print(f"{number} is not a prime number")
    if number == 2:
        print(f"{number} is a prime number")
    for n in range(2,int(number ** .5)+1) :
        if number % n ==0:
            print(f"{number} is not a prime number")
            return
    print(f"{number} is a prime number")

checkPrime2(97)#97 is a prime number
checkPrime2(17)#17 is a prime number  
checkPrime2(9)#9 is not a prime number 
checkPrime2(25)#25 is not a prime number 
checkPrime2(93)#93 is not a prime number 
checkPrime2(23)#93 is a prime number 

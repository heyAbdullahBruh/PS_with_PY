# Problem-1--->> FizzBuzz Print --> 
"""FizzBuzz
1)For numbers 1 to 100:
2)Print "Fizz" if divisible by 3,
3)"Buzz' if divisible by 5,
4)'FizzBuzz' if divisible by both."""

i =1
while i <=100:
    if i%3==0 and i%5==0 :
        print(f"FizzBuzz{i}")
    elif i%3==0:
        print(f'Fizz {i}')
    elif i%5==0 :
        print(f"Buzz {i}")
    
    i=i+1
    

#Build a function calculate(a, b, operator)

def calculate(a, b, operator="") :
    if operator== "+":
        print(a+b)
    elif operator== "-":
        print(a-b)
    elif operator== "*":
        print(a*b)
    elif operator== "/":
        print(a/b)
    elif operator== "%":
        print(a%b)
    elif operator== "^":
        print(a**b)
    else:
        print(a+b)    
    

calculate(2,3) #5
calculate(2,3,"+") #5
calculate(2,3,"*") #6
calculate(2,3,"/") #0.6666666666666666
calculate(2,3,"-") # -1
calculate(2,3,"^") # 8
calculate(2,3,"%") # 2


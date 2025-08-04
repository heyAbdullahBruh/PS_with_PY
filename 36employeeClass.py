# Problem -36 Make a Employee class--->

class Empolyeed :
    def __init__(self,name=str,salary=float,compnay=str):
        self.name=name
        self.compnay=compnay
        self.salary=salary
    def give_raise (self,amount):
        self.salary = self.salary +amount
    
    def detail(self) :
        return {"name":self.name,"salary":self.salary,"company":self.compnay}
    
empl1= Empolyeed('Harun Miah',40000,"Barun Org.")
print(empl1.detail())#{'name': 'Harun Miah', 'salary': 40000, 'company': 'Barun Org.'}
empl1.give_raise(3000)
print(empl1.detail()) #{'name': 'Harun Miah', 'salary': 43000, 'company': 'Barun Org.'}

